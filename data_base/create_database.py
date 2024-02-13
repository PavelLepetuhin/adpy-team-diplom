import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

from settings import USER, PASSWORD, HOST, DB_NAME

# Создание подключения к базе данных
connection_string = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(connection_string)
Base = sqlalchemy.orm.declarative_base()





# Создание классов для каждой таблицы
class BotUsers(Base):
    __tablename__ = 'botusers'
    id = Column(Integer, primary_key=True)
    vk_id = Column(BigInteger)
    city = Column(String(50))
    age = Column(Integer)
    gender = Column(Integer)


class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    botusers_id = Column(Integer, ForeignKey("botusers.id"))
    vk_id = Column(BigInteger)
    link = Column(String(200))
    name = Column(String(30))
    surname = Column(String(40))
    birth_date = Column(Date)
    city = Column(String(50))


class Top3Photo(Base):
    __tablename__ = 'top3photo'
    id = Column(Integer, primary_key=True)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    photo_1 = Column(String)
    photo_2 = Column(String)
    photo_3 = Column(String)


class Blacklist(Base):
    __tablename__ = 'blacklist'
    id = Column(Integer, primary_key=True)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    vk_id = Column(BigInteger)
    name = Column(String(30))
    surname = Column(String(40))
    date = Column(DateTime, default=datetime.datetime.utcnow)


# Base.metadata.drop_all(engine)
# Создание таблиц в базе данных
Base.metadata.create_all(engine)
