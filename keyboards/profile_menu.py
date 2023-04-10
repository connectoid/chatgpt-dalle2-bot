from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_1: KeyboardButton = KeyboardButton(text='🔢 Остаток заросов')
button_2: KeyboardButton = KeyboardButton(text='💰 Пополнить баланс')
button_3: KeyboardButton = KeyboardButton(text='🕑 История запросов')
button_4: KeyboardButton = KeyboardButton(text='🏠 Главное меню')

profile_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2],
                                              [button_3, button_4]],
                                    resize_keyboard=True)