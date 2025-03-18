from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from .models import Base, User, Prompt, ApiKey, Tariff
from config_data.config import load_config, Config

POOL_SIZE = 20
MAX_OVERFLOW = 0

config: Config = load_config()

db_user = config.db.db_user
db_password = config.db.db_password

database_url = f'postgresql://{db_user}:{db_password}@{config.db.db_host}:5432/{config.db.database}'
# database_url = f'postgresql://postgres:postgres@{config.db.db_host}:5432/{config.db.database}'

engine = create_engine(database_url, echo=False, pool_size=POOL_SIZE, max_overflow=MAX_OVERFLOW)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def init_tariffs():
    print('Start init tarrifs')
    session = Session()
    tariff = session.query(Tariff)
    first_tariff = session.query(Tariff).first()
    if first_tariff:
        print(f'Tariff id exists: {first_tariff}')
    else:
        print(f'Creating tariff')
        new_tariff = Tariff(
            name='Free',
            price=0,
            gpt_amount=10,
            dalle_amount=10
        )
        session.add(new_tariff)
        session.commit()


def add_user(tg_id, fname, lname):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    if user is None:
        new_user = User(tg_id=tg_id, fname=fname, lname=lname)
        session.add(new_user)
        session.commit()
        return True
    return False 


def get_user_id(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    return user.id


def set_user_openai_token(user_id, token):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    user.openai_token = token
    session.add(user)
    session.commit()


def save_user_prompt(user_id, prompt, is_chat_prompt=True):
    session = Session()
    new_prompt = session.query(Prompt).filter(Prompt.text == prompt, Prompt.owner == user_id).first()
    if new_prompt is None:
        new_prompt = Prompt(text=prompt, owner=user_id, is_chat_prompt=is_chat_prompt)
        session.add(new_prompt)
        session.commit()


def is_premium(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user.is_premium_user:
        return True
    return False


def change_gpt_count(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user.gpt_prompts_count > 0:
        user.gpt_prompts_count -= 1
        session.add(user)
        session.commit()
        return True
    else:
        return False


def change_dalle_count(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user.dalle_prompts_count > 0:
        user.dalle_prompts_count -= 1
        session.add(user)
        session.commit()
        return True
    else:
        return False


def get_remains(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    gpt_remains = user.gpt_prompts_count
    dalle_remains = user.dalle_prompts_count
    # text = (f'У вас осталось:\n'
    #        f'ChatGPT: {gpt_remains}\n'
    #        f'DALL-E2: {dalle_remains}\n'
    #)
    return gpt_remains, dalle_remains


def get_openai_api_key():
    session = Session()
    api_key = session.query(ApiKey).filter(ApiKey.active == True).first()
    return api_key.api_key_string


def disable_openai_api_key(api_key_string):
    session = Session()
    api_key = session.query(ApiKey).filter(ApiKey.api_key_string == api_key_string).first()
    api_key.active = False
    session.add(api_key)
    session.commit()


def get_user_lang(user_id):
    session = Session()
    user_lang = session.query(User).filter(User.id == user_id).first().language
    return user_lang


def set_user_lang(user_id, user_lang):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    user.language = user_lang
    session.add(user)
    session.commit()

def set_user_tariff(user_id, tariff_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    user_tariff = session.query(Tariff).filter(Tariff.id == tariff_id).first()
    user.tariff_id = tariff_id
    print(user_tariff, tariff_id)
    user.gpt_prompts_count = user_tariff.gpt_amount
    user.dalle_prompts_count = user_tariff.dalle_amount
    session.add(user)
    session.commit()

def get_user_tariff(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()    
    tariff = user.tariff
    if tariff:
        return tariff
    return None
    
def get_tariffs():
    session = Session()
    tariffs = session.query(Tariff).all()
    print(f'Tariffs from ORM: {tariffs}')
    return tariffs

def get_tariff_by_id(tariff_id):
    session = Session()
    tariff = session.query(Tariff).filter(Tariff.id == tariff_id).first()
    return tariff

def get_recent_prompts(user_id, count):
    session = Session()
    recent_prompts = session.query(Prompt).filter(Prompt.owner == user_id).all()
    return recent_prompts[-count:]