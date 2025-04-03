from time import sleep

from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message

from keyboards.main_menu import get_main_menu
from config_data.config import Config, load_config
from utils.parser import get_events
from utils.tools import create_message_text, compare_and_update_dict, add_userid_to_file

router = Router()
config: Config = load_config()


@router.message(~F.text)
async def content_type_example(msg: Message):
    await msg.answer('👍')


@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
        user_id = message.from_user.id
        add_userid_to_file(user_id)
        await message.answer(
        text='Hello message',
        reply_markup=get_main_menu())


@router.message(Text(text='Проверить'))
async def process_button_1_command(message: Message):
    events = get_events()
    if compare_and_update_dict(events):
        message_text = create_message_text(events)
        if message_text:
            await message.answer(
                text=message_text, 
                reply_markup=get_main_menu()
            )
        else:
            await message.answer(
                text='Произошла ошибка, смотри логи', 
                reply_markup=get_main_menu()
            )
    else:
         await message.answer(
                text='Данные не изменились', 
                reply_markup=get_main_menu()
            )