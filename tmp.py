import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
from collections import defaultdict
from datetime import datetime, timedelta



file = open('config.json', 'r')
config = json.load(file)

openai.api_key = config['openai']
bot = Bot(config['token'])
dp = Dispatcher(bot)
messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": ""},
        {"role": "assistant", "content": ""},
        #{"role": "user", "content": "Where was it played?"}
    ]


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

#Telegram

#Команды

#показать список команд
@dp.message_handler(commands=['help'])
async def show_commands(message: types.Message):
    help_message = "/start - Приветственное сообщение\n/clear - Очистить чат\n/help - Показать список команд"
    await message.answer(help_message, reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(btn1))

#вступление
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("")

#Очиска чата
@dp.message_handler(commands=['clear'])
async def clear_chat(message: types.Message):
    global messages
    messages = []
    await message.answer("Чат очищен.")

#Доп инфо про бота
@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.answer()


#кнопки
btn1 = types.KeyboardButton("/help - Все команды в боте")

#сообщения в группе
@dp.message_handler(content_types=["text"], chat_type=["group", "supergroup"])
async def send_group_message(message: types.Message):
    bot_info = await message.bot.get_me()
    if f'@{bot_info.username}' in message.text:
        update(messages, "user", message.text)
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature=1,
        #max_tokens=4096
        )
        await message.answer(response['choices'][0]['message']['content'])
        # сохранение сообщения в лог-файл
        user_id = message.from_user.id
        user_name = message.from_user.username if message.from_user.username else message.from_user.first_name
        message_text = message.text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = {
            "timestamp": timestamp,
            "user_id": user_id,
            "user_name": user_name,
            "message": message_text
        }
        with open("updates.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
            print(log_data)

    else:
        # сохранение сообщения в лог-файл
        user_id = message.from_user.id
        user_name = message.from_user.username if message.from_user.username else message.from_user.first_name
        message_text = message.text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = {
            "timestamp": timestamp,
            "user_id": user_id,
            "user_name": user_name,
            "message": message_text
        }
        with open("updates.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
            print(log_data)


#сообщения в личке
@dp.message_handler(content_types=["text"], chat_type=["private"])
async def echo(message : types.Message):
    update(messages, "user", message.text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature = 0.5,
        #max_tokens=4096
        presence_penalty = 1
    )
    await message.answer(response['choices'][0]['message']['content'])
    # сохранение сообщения в лог-файл
    user_id = message.from_user.id
    user_name = message.from_user.username if message.from_user.username else message.from_user.first_name
    message_text = message.text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = {
        "timestamp": timestamp,
"user_id": user_id,
        "user_name": user_name,
        "message": message_text
    }
    with open("updates.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
        print(log_data)
executor.start_polling(dp, skip_updates=True)





#Ограничение сообщений
# словарь для хранения количества сообщений и времени последнего сообщения для каждого пользователя
user_messages = defaultdict(lambda: {"count": 0, "last_time": None})

# максимальное количество сообщений, разрешенных для каждого пользователя в определенный промежуток времени
max_messages = 10

# промежуток времени, в течение которого ограничение на сообщения актуально
time_frame = timedelta(hours=2)

# обработчик сообщений в личных чатах и групповых чатах
@dp.message_handler(content_types=["text"], chat_type=["private","group", "supergroup"])
async def echo(message: types.Message):
    # получаем ID пользователя
    user_id = message.from_user.id

    # получаем текущее время
    now = datetime.now()

    # получаем количество сообщений и время последнего сообщения для пользователя
    user_info = user_messages[user_id]

    # если пользователь превысил лимит сообщений, уведомляем его и выходим из функции
    if user_info["count"] >= max_messages and now - user_info["last_time"] <= time_frame:
        await message.answer("Вы превысили лимит сообщений. Пожалуйста, попробуйте позже.")
        return

    # обновляем количество сообщений и время последнего сообщения пользователя
    user_info["count"] += 1
    user_info["last_time"] = now

    # оставшаяся часть кода обработки сообщений...