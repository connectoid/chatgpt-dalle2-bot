from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_1: KeyboardButton = KeyboardButton(text='⬅️ В главное меню')
button_2: KeyboardButton = KeyboardButton(text='🔁 Повторить')

answer_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1]],
                                    resize_keyboard=True,
                                    input_field_placeholder='prompt')

answer_repeat_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]],
                                    resize_keyboard=True,
                                    input_field_placeholder='prompt')