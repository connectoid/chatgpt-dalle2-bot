from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_en import LEXICON_COMMANDS
from lexicon.lexicon import COMMAND
from database.orm import get_user_lang

# Функция для настройки кнопки Menu бота
async def set_commands_menu(bot: Bot, user_id = None):
      if user_id:
            lang = get_user_lang(user_id)
            await bot.delete_my_commands()
            main_menu_commands = [BotCommand(
                                    command=command,
                                    description=description
                              ) for command,
                                    description in COMMAND[lang].items()]
            await bot.set_my_commands(main_menu_commands)