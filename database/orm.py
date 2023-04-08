from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from .models import Base, User, Prompt
from config_data.config import load_config, Config

config: Config = load_config()

database_url = f'postgresql://postgres:postgres@{config.db.db_host}:5432/{config.db.database}'

engine = create_engine(database_url, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_user(tg_id, fname, lname):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    if user is None:
        new_user = User(tg_id=tg_id, fname=fname, lname=lname)
        session.add(new_user)
        session.commit()


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