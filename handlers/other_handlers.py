from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_en import UNRECOGNIZED_COMMAND
from lexicon.lexicon import BUTTON, MESSAGE
from database.orm import get_user_id, get_user_lang

router: Router = Router()


@router.message()
async def send_echo(message: Message):
    user_id = get_user_id(message.from_user.id)
    lang = get_user_lang(user_id)
    await message.answer(MESSAGE[lang]['UNRECOGNIZED_COMMAND'])


