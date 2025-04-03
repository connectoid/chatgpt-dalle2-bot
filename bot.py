import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from utils.parser import get_events
from utils.tools import compare_and_update_dict, create_message_text, read_ids_from_file
from keyboards.main_menu import get_main_menu


REQUEST_INTERVAL = 60

logger = logging.getLogger(__name__)
storage = MemoryStorage()

scheduler = AsyncIOScheduler()

config = load_config('.env')

BOT_TOKEN = config.tg_bot.token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    logging.basicConfig(
        level=logging.INFO,
        filename = "botlog.log",
        filemode='a',
        format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
        datefmt='%H:%M:%S',
        )
    logger.info('Starting bot')
    
    config: Config = load_config()

    # bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    # dp = Dispatcher(storage=storage)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await schedule_jobs()
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    print('Start polling')
    await dp.start_polling(bot)


async def request_events(dp: Dispatcher):
    ids = read_ids_from_file()
    print('Запрашиваем события через планировщик')
    events = get_events()
    if events:
        if compare_and_update_dict(events):
            message_text = create_message_text(events)
            if message_text:
                for id in ids:
                    await bot.send_message(
                        chat_id=id,
                        text=message_text, 
                        reply_markup=get_main_menu()
                    )
            else:
                for id in ids:
                    await bot.send_message(
                        chat_id=id,
                        text='Exception in scheduler', 
                        reply_markup=get_main_menu()
                    )
        else:
            print('No changes')
    else:
        for id in ids:
            await bot.send_message(
                chat_id=id,
                text='Произошла ошибка ,смотри логи', 
                reply_markup=get_main_menu()
            )


async def schedule_jobs():
    scheduler.add_job(request_events, 'interval', seconds = REQUEST_INTERVAL, args=(dp,))



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')