from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_en import HELP_BUTTON, PROFILE_BUTTON
from lexicon.lexicon import BUTTON
from database.orm import get_user_lang


def get_main_menu(user_id):
    lang = get_user_lang(user_id)
    button_1: KeyboardButton = KeyboardButton(text='🤖 ChatGPT-4')
    button_2: KeyboardButton = KeyboardButton(text='👨‍🎨 DALL-E3')
    button_3: KeyboardButton = KeyboardButton(text=BUTTON[lang]['HELP_BUTTON'])
    button_4: KeyboardButton = KeyboardButton(text=BUTTON[lang]['PROFILE_BUTTON'])

    main_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1, button_2],
                                                [button_3, button_4]],
                                        resize_keyboard=True,
                                        input_field_placeholder='prompt')
    return main_menu_keyboard