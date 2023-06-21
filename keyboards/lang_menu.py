from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_en import REMAINS_BUTTON, TARIFF_BUTTON, HISTORY_BUTTON, MAIN_MENU_BUTTON
from lexicon.lexicon import BUTTON
from database.orm import get_user_lang

def get_lang_menu(user_id):
    lang = get_user_lang(user_id)
    button_1: KeyboardButton = KeyboardButton(text=BUTTON[lang]['RUS_LANG_BUTTON'])
    button_2: KeyboardButton = KeyboardButton(text=BUTTON[lang]['ENG_LANG_BUTTON'])

    lang_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1, button_2]],
                                        resize_keyboard=True)
    return lang_menu_keyboard