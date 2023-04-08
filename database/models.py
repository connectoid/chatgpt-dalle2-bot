from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
 

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=True)
    lname = Column(String, nullable=True)
    tg_id = Column(BigInteger, nullable=False)
    openai_token = Column(String, nullable=True)
    free_gpt_promts_count = Column(Integer, default=10)
    free_dalle_promts_count = Column(Integer, default=10)
    prepaid_gpt_promts_count = Column(Integer, default=0)
    prepaid_dalle_promts_count = Column(Integer, default=0)
    prompts = relationship('Prompt', backref='users', lazy=True)
    is_premium_user = Column(Boolean, default=False)
    register_date = Column(DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return self.tg_id


class Prompt(Base):
    __tablename__ = 'prompt'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_chat_prompt = Column(Boolean, default=True)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return self.text