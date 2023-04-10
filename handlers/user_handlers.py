from time import sleep

import openai

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

from lexicon.lexicon_ru import LEXICON_HELP, GPT_CHAT_TEXT, DALLE_CHAT_TEXT, START_MESSAGE
from database.orm import (add_user, get_user_id, set_user_openai_token, save_user_prompt,
                          change_gpt_count, change_dalle_count, get_remains, set_user_tariff)
from keyboards.main_menu import main_menu_keyboard
from keyboards.answer_menu import answer_menu_keyboard
from keyboards.profile_menu import profile_menu_keyboard
from keyboards.bottom_post_kb import create_bottom_keyboard
from services.chatgpt import get_answer
from services.dalle2 import get_picture
from config_data.config import Config, load_config



storage = MemoryStorage()
router = Router()
config: Config = load_config()
test_openai_token = config.open_ai.key


class FSMChatGPT(StatesGroup):
    gpt_text_prompt = State()


class FSMDallE2(StatesGroup):
    dalle2_text_prompt = State()


@router.message(CommandStart(), StateFilter(default_state))
@router.message(Text(text='🏠 Главное меню'))
async def process_start_command(message: Message):
    fname = message.from_user.first_name
    lname = message.from_user.last_name
    tg_id = message.from_user.id
    add_user(tg_id, fname, lname)
    user_id = get_user_id(message.from_user.id)
    set_user_openai_token(user_id, test_openai_token)
    await message.answer(
        text=START_MESSAGE,
        reply_markup=main_menu_keyboard
    )


@router.message(Command(commands='help'), StateFilter(default_state))
@router.message(Text(text='🆘 Помощь'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HELP, disable_web_page_preview=True)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Вы вышли из диалога', reply_markup=main_menu_keyboard)
    await state.clear()


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command_notstate(message: Message):
    await message.answer(text='В данный момент вы не ведёте диалог. '
                         'Выберите в главном меню ИИ для диалога')


@router.message(CommandStart(), ~StateFilter(default_state))
@router.message(Command(commands='profile'), ~StateFilter(default_state))
@router.message(Command(commands='help'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Эта команда недоступна в режиме диалога с ИИ. '
                                'Для вызова данной команды нужно выйти из диалога', reply_markup=answer_menu_keyboard)
    await state.clear()



""" Узнать как объединять фильтры в одном хэндлере """
@router.message(Text(text='⬅️ Назад в главное меню'), StateFilter(FSMChatGPT.gpt_text_prompt))
@router.message(Text(text='⬅️ Назад в главное меню'), StateFilter(FSMDallE2.dalle2_text_prompt))
async def process_back_command(message: Message, state: FSMContext):
    await message.answer(text='Вы вышли из диалога',
                         reply_markup=main_menu_keyboard)
    await state.clear()


@router.message(Text(text='🤖 ChatGPT'), StateFilter(default_state))
async def process_send_gpt_prompt_command(message: Message, state: FSMContext):
    await message.answer(text=GPT_CHAT_TEXT,
                         reply_markup=answer_menu_keyboard)
    await state.set_state(FSMChatGPT.gpt_text_prompt)
    


@router.message(StateFilter(FSMChatGPT.gpt_text_prompt))
async def process_gpt_prompt_sent(message: Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    user_id = get_user_id(message.from_user.id)
    if not change_gpt_count(user_id):
        await message.answer(text='У вас не осталось оплаченных запросов, выйдети из диалога и '\
                             'выберите тариф в разделе Профиль')
    else:
        save_user_prompt(user_id, message.text, is_chat_prompt=True)
        text_answer = get_answer(message.text)
        await message.answer(text=text_answer, reply_markup=answer_menu_keyboard)


@router.message(Text(text='👨‍🎨 DALL-E2'), StateFilter(default_state))
async def process_send_dalle2_prompt_command(message: Message, state: FSMContext):
    await message.answer(text=DALLE_CHAT_TEXT,
                         reply_markup=answer_menu_keyboard)
    await state.set_state(FSMDallE2.dalle2_text_prompt)
    


@router.message(StateFilter(FSMDallE2.dalle2_text_prompt))
async def process_dalle2_prompt_sent(message: Message, state: FSMContext):
    await state.update_data(prompt=message.text)
    user_id = get_user_id(message.from_user.id)
    if not change_dalle_count(user_id):
        await message.answer(text='У вас не осталось оплаченных запросов, выйдети из диалога и '\
                             'выберите тариф в разделе Профиль')
    else:
        save_user_prompt(user_id, message.text, is_chat_prompt=False)
        image_answer = get_picture(message.text)
        await message.answer_photo(photo=image_answer, reply_markup=answer_menu_keyboard)


@router.message(Command(commands='profile'), StateFilter(default_state))
@router.message(Text(text='ℹ️ Профиль'))
async def process_profile_menu_command(message: Message):
    user_id = get_user_id(message.from_user.id)
    await message.answer(text='Выберите раздел', reply_markup=profile_menu_keyboard)


@router.message(Text(text='🔢 Остаток заросов'))
async def process_remains_command(message: Message):
        user_id = get_user_id(message.from_user.id)
        text = get_remains(user_id)
        await message.answer(text=text, reply_markup=profile_menu_keyboard)


@router.message(Text(text='💰 Выбрать тариф'))
async def process_show_tariffs_command(callback: CallbackQuery):
    user_id = get_user_id(callback.from_user.id)
    await callback.answer(text='Выберите тариф (бесплатно в тестовом режиме):',
                          reply_markup=create_bottom_keyboard(
                            'Тариф "Лайт" (25 запросов)',
                            'Тариф "Оптима" (50 запросов)', 
                            'Тариф "Макс" (100 запросов)'),
                            parse_mode='HTML')


@router.callback_query(Text(startswith='Тариф'))
async def process_choice_tariff(callback: CallbackQuery):
    tariff = callback.data.split('(')[1].split()[0]
    tarii_name = callback.data
    user_id = get_user_id(callback.from_user.id)
    set_user_tariff(user_id, tariff)
    await callback.message.answer(text=f'Выбран тариф {tarii_name}')
    #await callback.message.edit_reply_markup(reply_markup=create_bottom_keyboard(
    #                id, 'Подробно', '❎ Из избранного'))
    #await callback.answer()


@router.message(Text(text='🕑 История запросов'))
async def process_remains_command(message: Message):
        #user_id = get_user_id(message.from_user.id)
        text = '👷‍♂️ Данный раздел пока в разработке'
        await message.answer(text=text, reply_markup=profile_menu_keyboard)



@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')
