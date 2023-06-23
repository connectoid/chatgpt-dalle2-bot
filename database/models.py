from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
 
class Tariff(Base):
    __tablename__ = 'tariff'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    gpt_amount = Column(Integer, nullable=False)
    dalle_amount = Column(Integer, nullable=False)
    users = relationship("User", back_populates="tariff")


    def __repr__(self):
        return self.name

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=True)
    lname = Column(String, nullable=True)
    tg_id = Column(BigInteger, nullable=False)
    gpt_prompts_count = Column(Integer)
    dalle_prompts_count = Column(Integer)
    tariff_id = Column(Integer, ForeignKey('tariff.id'))
    tariff = relationship('Tariff', back_populates='users')
    prompts = relationship('Prompt', backref='users', lazy=True)
    register_date = Column(DateTime, default=datetime.now, nullable=False)
    language = Column(String, nullable=False, default='ru')

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
    

class ApiKey(Base):
    __tablename__ = 'api_key'
    id = Column(Integer, primary_key=True)
    api_key_string = Column(String, nullable=False)
    active = Column(Boolean, default=True)