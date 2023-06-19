from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import Config, load_config


config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


ADMIN_CHAT_ID = config.tg_bot.admin_chat_id


@dp.message()
async def send_to_admin(message: types.Message, text: str, parse_mode):
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=text, parse_mode=parse_mode)
