from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_en import TO_MAIN_MENU_BUTTON, REPEAT_BUTTON
from lexicon.lexicon import BUTTON
from database.orm import get_user_lang

def get_answer_menu(user_id):
    lang = get_user_lang(user_id)
    button_1: KeyboardButton = KeyboardButton(text=BUTTON[lang]['TO_MAIN_MENU_BUTTON'])

    answer_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1]],
                                        resize_keyboard=True,
                                        input_field_placeholder='prompt')

    return answer_menu_keyboard


def get_answer_repeat_menu(user_id):
    lang = get_user_lang(user_id)
    button_1: KeyboardButton = KeyboardButton(text=BUTTON[lang]['TO_MAIN_MENU_BUTTON'])
    button_2: KeyboardButton = KeyboardButton(text=BUTTON[lang]['REPEAT_BUTTON'])

    answer_repeat_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1, button_2]],
                                        resize_keyboard=True,
                                        input_field_placeholder='prompt')
    return answer_repeat_menu_keyboard