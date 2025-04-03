from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


def get_main_menu():
    button_1: KeyboardButton = KeyboardButton(text='Проверить')
#     button_2: KeyboardButton = KeyboardButton(text='Button 2')
#     button_3: KeyboardButton = KeyboardButton(text='Button 3')
#     button_4: KeyboardButton = KeyboardButton(text='Button 4')

    main_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=[[button_1],],
                                        resize_keyboard=True,
                                        input_field_placeholder='placeholder')
    return main_menu_keyboard