from time import sleep

import openai

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

from lexicon.lexicon_en import (LEXICON_HELP, GPT_CHAT_TEXT, DALLE_CHAT_TEXT, START_MESSAGE,
                                FEEDBACK_TEXT, FEEDBACK_SENT, MAIN_MENU_BUTTON, HELP_BUTTON, HISTORY_BUTTON,
                                TO_MAIN_MENU_BUTTON, REMAINS_BUTTON, REPEAT_BUTTON, PROFILE_BUTTON,
                                TARIFF_BUTTON)
from lexicon.lexicon import MESSAGE, BUTTON, TARIFF, BROADCAST
from database.orm import (add_user, get_user_id, set_user_openai_token, save_user_prompt,
                          change_gpt_count, change_dalle_count, get_remains, set_user_tariff,
                          set_user_lang, get_user_lang)
from keyboards.main_menu import get_main_menu
from keyboards.answer_menu import get_answer_menu, get_answer_repeat_menu
from keyboards.profile_menu import get_profile_menu
from keyboards.bottom_post_kb import create_bottom_keyboard
from keyboards.lang_menu import get_lang_menu
from keyboards.commands_menu import set_commands_menu
from services.chatgpt import get_answer
from services.dalle2 import get_picture
from config_data.config import Config, load_config
from utils.utils import send_to_admin

storage = MemoryStorage()
router = Router()
config: Config = load_config()


class FSMChatGPT(StatesGroup):
    gpt_text_prompt = State()


class FSMDallE2(StatesGroup):
    dalle2_text_prompt = State()

class FSMFeedback(StatesGroup):
    feedback_text = State()

lang = 'ru'


@router.message(CommandStart(), StateFilter(default_state))
@router.message(Text(text=BUTTON['ru']['MAIN_MENU_BUTTON']))
@router.message(Text(text=BUTTON['en']['MAIN_MENU_BUTTON']))
async def process_start_command(message: Message, bot: Bot):
    fname = message.from_user.first_name
    lname = message.from_user.last_name
    tg_id = message.from_user.id
    add_user(tg_id, fname, lname)
    user_id = get_user_id(message.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    await set_commands_menu(bot, user_id)
    await message.answer(
        text=MESSAGE[lang]['START_MESSAGE'],
        reply_markup=get_main_menu(user_id)
    )

@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    user_id = get_user_id(message.from_user.id)
    await message.answer(text=MESSAGE[lang]['EXIT_DIALOGUE'], reply_markup=get_main_menu(user_id))
    await state.clear()

@router.message(CommandStart(), ~StateFilter(default_state))
@router.message(Command(commands='profile'), ~StateFilter(default_state))
@router.message(Command(commands='help'), ~StateFilter(default_state))
@router.message(Command(commands='feedback'), ~StateFilter(default_state))
@router.message(Command(commands='lang'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    user_id = get_user_id(message.from_user.id)
    await message.answer(text=MESSAGE[lang]['DENIED_IN_DIALOGUE'],
                                reply_markup=get_answer_menu(user_id))

@router.message(Command(commands='help'), StateFilter(default_state))
@router.message(Text(text=BUTTON['ru']['HELP_BUTTON']))
@router.message(Text(text=BUTTON['en']['HELP_BUTTON']))
async def process_help_command(message: Message):
    await message.answer(text=MESSAGE[lang]['LEXICON_HELP'], disable_web_page_preview=True)

@router.message(Command(commands='lang'), StateFilter(default_state))
async def process_lang_command(callback: CallbackQuery):
    user_id = get_user_id(callback.from_user.id)
    await callback.answer(text=MESSAGE[lang]['LANG'],
                          reply_markup=create_bottom_keyboard(
                            BUTTON[lang]['RUS_LANG_BUTTON'],
                            BUTTON[lang]['ENG_LANG_BUTTON'],),
                            parse_mode='HTML'
                        )

@router.callback_query(Text(endswith='(ru)'))
@router.callback_query(Text(endswith='(en)'))
async def process_choice_tariff(callback: CallbackQuery, bot: Bot):
    chosen_lang = callback.data.split(' ')[-1].strip('()')
    lang_name = callback.data
    user_id = get_user_id(callback.from_user.id)
    global lang
    lang = chosen_lang
    set_user_lang(user_id, chosen_lang)
    await set_commands_menu(bot, user_id)
    await callback.message.answer(text=f'{MESSAGE[lang]["LANG_CHOSEN"]} {lang_name}',
                                  reply_markup=get_main_menu(user_id))


@router.message(Command(commands='feedback'), StateFilter(default_state))
async def process_feedback_command(message: Message, state: FSMContext):
    await message.answer(text=MESSAGE[lang]['FEEDBACK_TEXT'])
    await state.set_state(FSMFeedback.feedback_text)


@router.message(StateFilter(FSMFeedback.feedback_text), StateFilter(FSMFeedback.feedback_text))
async def process_feedback_sent(message: Message, state: FSMContext):
    await state.update_data(message_text=message.text)
    user_tg_id = message.from_user.id
    user_name = f'{message.from_user.first_name} {message.from_user.last_name}'
    user_login = message.from_user.username
    user_link = f'[{user_login}](tg://user?id={str(user_tg_id)})'
    await send_to_admin(
            message,
            text=f'Сообщение от пользователя {user_name} ({user_link}): {message.text}',
            parse_mode='Markdown'
        )
    await message.answer(text=FEEDBACK_SENT)
    await state.clear()


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command_notstate(message: Message):
    await message.answer(text=MESSAGE[lang]['NOT_IN_DIALOGUE'])


""" Узнать как объединять фильтры в одном хэндлере """
@router.message(Text(text=BUTTON['ru']['TO_MAIN_MENU_BUTTON']), StateFilter(FSMChatGPT.gpt_text_prompt))
@router.message(Text(text=BUTTON['en']['TO_MAIN_MENU_BUTTON']), StateFilter(FSMChatGPT.gpt_text_prompt))
@router.message(Text(text=BUTTON['ru']['TO_MAIN_MENU_BUTTON']), StateFilter(FSMDallE2.dalle2_text_prompt))
@router.message(Text(text=BUTTON['en']['TO_MAIN_MENU_BUTTON']), StateFilter(FSMDallE2.dalle2_text_prompt))
async def process_back_command(message: Message, state: FSMContext):
    user_id = get_user_id(message.from_user.id)
    await message.answer(text=MESSAGE[lang]['EXIT_DIALOGUE'],
                         reply_markup=get_main_menu(user_id))
    await state.clear()


@router.message(Text(text='🤖 ChatGPT'), StateFilter(default_state))
async def process_send_gpt_prompt_command(message: Message, state: FSMContext):
    user_id = get_user_id(message.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    await message.answer(text=MESSAGE[lang]['GPT_CHAT_TEXT'],
                         reply_markup=get_answer_menu(user_id))
    await state.set_state(FSMChatGPT.gpt_text_prompt)
    


@router.message(StateFilter(FSMChatGPT.gpt_text_prompt), ~Text(text=BUTTON[lang]['REPEAT_BUTTON']))
async def process_gpt_prompt_sent(message: Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    user_id = get_user_id(message.from_user.id)
    user_name = f'{message.from_user.first_name} {message.from_user.last_name}'
    if not change_gpt_count(user_id):
        await message.answer(text=MESSAGE[lang]['LIMIT_RICHED'])
    else:
        save_user_prompt(user_id, message.text, is_chat_prompt=True)
        text_answer = get_answer(message.text, user_id)
        await message.answer(text=str(text_answer), reply_markup=get_answer_repeat_menu(user_id), parse_mode="markdown")
        if str(message.from_user.id) != str(config.tg_bot.admin_chat_id):
            await send_to_admin(
                message,
                text=f'Пользователь {user_name} '\
                f'отправил запрос:\n"{message.text}" \n'\
                f'и получил ответ:\n"{text_answer}"'
                )

@router.message(Text(text=BUTTON['ru']['REPEAT_BUTTON']), StateFilter(FSMChatGPT.gpt_text_prompt))
@router.message(Text(text=BUTTON['en']['REPEAT_BUTTON']), StateFilter(FSMChatGPT.gpt_text_prompt))
async def process_repeat_gpt_prompt_command(message: Message, state: FSMContext):
    prompt_dict = await state.get_data()
    prompt = prompt_dict['prompt']
    user_id = get_user_id(message.from_user.id)
    user_name = f'{message.from_user.first_name} {message.from_user.last_name}'
    if not change_gpt_count(user_id):
        await message.answer(text=MESSAGE[lang]['LIMIT_RICHED'])
    else:
        text_answer = get_answer(prompt, user_id)
        await message.answer(text=str(text_answer), reply_markup=get_answer_repeat_menu(user_id), parse_mode="markdown")
        if str(message.from_user.id) != str(config.tg_bot.admin_chat_id):
            await send_to_admin(
                message,
                text=f'Пользователь {user_name} '\
                f'повторил запрос и получил ответ:\n"{text_answer}"'
                )


@router.message(Text(text='👨‍🎨 DALL-E2'), StateFilter(default_state))
async def process_send_dalle2_prompt_command(message: Message, state: FSMContext):
    user_id = get_user_id(message.from_user.id)
    await message.answer(text=MESSAGE[lang]['DALLE_CHAT_TEXT'],
                         reply_markup=get_answer_menu(user_id))
    await state.set_state(FSMDallE2.dalle2_text_prompt)
    


@router.message(StateFilter(FSMDallE2.dalle2_text_prompt), ~Text(text=BUTTON[lang]['REPEAT_BUTTON']))
async def process_dalle2_prompt_sent(message: Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    user_id = get_user_id(message.from_user.id)
    if not change_dalle_count(user_id):
        await message.answer(MESSAGE[lang]['LIMIT_RICHED'])
    else:
        save_user_prompt(user_id, message.text, is_chat_prompt=False)
        image_answer = get_picture(message.text)
        await message.answer_photo(photo=image_answer, reply_markup=get_answer_repeat_menu(user_id))


@router.message(Text(text=BUTTON['ru']['REPEAT_BUTTON']), StateFilter(FSMDallE2.dalle2_text_prompt))
@router.message(Text(text=BUTTON['en']['REPEAT_BUTTON']), StateFilter(FSMDallE2.dalle2_text_prompt))
async def process_repeat_dalle2_prompt_command(message: Message, state: FSMContext):
    prompt_dict = await state.get_data()
    prompt = prompt_dict['prompt']
    user_id = get_user_id(message.from_user.id)
    if not change_gpt_count(user_id):
        await message.answer(MESSAGE[lang]['LIMIT_RICHED'])
    else:
        image_answer = get_picture(prompt)
        await message.answer_photo(photo=image_answer, reply_markup=get_answer_repeat_menu(user_id))


@router.message(Command(commands='profile'), StateFilter(default_state))
@router.message(Text(text=BUTTON['ru']['PROFILE_BUTTON']))
@router.message(Text(text=BUTTON['en']['PROFILE_BUTTON']))
async def process_profile_menu_command(message: Message):
    user_id = get_user_id(message.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    await message.answer(text=MESSAGE[lang]['CHOOSE_SECTION'],
                         reply_markup=get_profile_menu(user_id))


@router.message(Text(text=BUTTON['ru']['REMAINS_BUTTON']))
@router.message(Text(text=BUTTON['en']['REMAINS_BUTTON']))
async def process_remains_command(message: Message):
        user_id = get_user_id(message.from_user.id)
        global lang
        lang = get_user_lang(user_id)
        gpt_remains, dalle_remains = get_remains(user_id)
        remains_phrase = MESSAGE[lang]['PROMPTS_REMAINS']
        text = (f'{remains_phrase}\n'
            f'ChatGPT: {gpt_remains}\n'
            f'DALL-E2: {dalle_remains}\n')
        await message.answer(text=text, reply_markup=get_profile_menu(user_id))


@router.message(Text(text=BUTTON['ru']['TARIFF_BUTTON']))
@router.message(Text(text=BUTTON['en']['TARIFF_BUTTON']))
async def process_show_tariffs_command(callback: CallbackQuery):
    user_id = get_user_id(callback.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    await callback.answer(text=MESSAGE[lang]['CHOOSE_TARIFF'],
                          reply_markup=create_bottom_keyboard(
                            TARIFF[lang]['tariff-1'],
                            TARIFF[lang]['tariff-2'], 
                            TARIFF[lang]['tariff-3']),
                            parse_mode='HTML')


@router.callback_query(Text(startswith='Тариф'))
@router.callback_query(Text(startswith='Tariff'))
async def process_choice_tariff(callback: CallbackQuery):
    tariff = callback.data.split('(')[1].split()[0]
    tarii_name = callback.data
    user_id = get_user_id(callback.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    set_user_tariff(user_id, tariff)
    TARIFF_SELECTED = MESSAGE[lang]['TARIFF_SELECTED']
    await callback.message.answer(text=f'{TARIFF_SELECTED} {tarii_name}')


@router.message(Text(text=BUTTON['ru']['HISTORY_BUTTON']))
@router.message(Text(text=BUTTON['en']['HISTORY_BUTTON']))
async def process_remains_command(message: Message):
        user_id = get_user_id(message.from_user.id)
        text = MESSAGE[lang]['UNDER_DEVELOPMENT']
        await message.answer(text=text, reply_markup=get_profile_menu(user_id))



@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


@router.message(Command(commands='broadcast'), StateFilter(default_state))
async def process_feedback_command(message: Message, bot: Bot):
    user_id = get_user_id(message.from_user.id)
    global lang
    lang = get_user_lang(user_id)
    text=BROADCAST[lang]['whats_new']
    users = ['101676827']
    for user_id in users:
        await bot.send_message(chat_id=user_id, text=text)
