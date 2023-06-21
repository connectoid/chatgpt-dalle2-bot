from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_en import REMAINS_BUTTON, TARIFF_BUTTON, HISTORY_BUTTON, MAIN_MENU_BUTTON
from lexicon.lexicon import BUTTON
from database.orm import get_user_lang

def get_profile_menu(user_id):
    lang = get_user_lang(user_id)
    button_1: KeyboardButton = KeyboardButton(text=BUTTON[lang]['REMAINS_BUTTON'])
    button_2: KeyboardButton = KeyboardButton(text=BUTTON[lang]['TARIFF_BUTTON'])
    button_3: KeyboardButton = KeyboardButton(text=BUTTON[lang]['HISTORY_BUTTON'])
    button_4: KeyboardButton = KeyboardButton(text=BUTTON[lang]['MAIN_MENU_BUTTON'])

    profile_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1, button_2],
                                                [button_3, button_4]],
                                        resize_keyboard=True)
    return profile_menu_keyboard