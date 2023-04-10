from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_1: KeyboardButton = KeyboardButton(text='🤖 ChatGPT')
button_2: KeyboardButton = KeyboardButton(text='👨‍🎨 DALL-E2')
button_3: KeyboardButton = KeyboardButton(text='🆘 Помощь')
button_4: KeyboardButton = KeyboardButton(text='ℹ️ Профиль')

main_menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2],
                                              [button_3, button_4]],
                                    resize_keyboard=True,
                                    input_field_placeholder='prompt')