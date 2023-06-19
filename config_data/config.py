from dataclasses import dataclass
from environs import Env

#from database.orm import get_openai_token

@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных
    

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту 
    admin_chat_id: str


#@dataclass
#class OpenAI:
#    key: str


@dataclass
class Config:
    tg_bot: TgBot
    # open_ai: OpenAI
    db: DatabaseConfig


def load_config(path: str = None):

    env: Env = Env()
    env.read_env(path)

    #open_ai = get_openai_token()
    #print('*******', open_ai)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_chat_id=env('ADMIN_CHAT_ID')),
                  #open_ai=OpenAI(key=env('OPENAI_TOKEN')),
                  #open_ai=open_ai,
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))
