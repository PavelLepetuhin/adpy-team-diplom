
from create_database import Favourite, BotUsers, Top3Photo, Blacklist
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import USER, PASSWORD, HOST, DB_NAME


# Создание подключения к базе данных
connection_string = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(connection_string)
Base = declarative_base()


def add_bot_users(vk_id, city, age, gender):
    try:
        user = BotUsers(vk_id=vk_id, city=city, age=age, gender=gender)
        Base.session.add(user)
        Base.session.commit()
    except:
        Base.session.rollback()


def add_favorite(botusers_id, vk_id, name, surname, birth_date, city):
    try:
        favorite = Favourite(botusers_id=botusers_id, vk_id=vk_id, name=name, surname=surname, birth_date=birth_date, city=city)
        Base.session.add(favorite)
        Base.session.commit()
    except:
        Base.session.rollback()


def add_top3(favourites_id, photo_1, photo_2, photo_3):
    try:
        top3 = Top3Photo(favourites_id=favourites_id, photo_1=photo_1, photo_2=photo_2, photo_3=photo_3)
        Base.session.add(top3)
        Base.session.commit()
    except:
        Base.session.rollback()


def add_blacklist(favorite_id, vk_id, name, surname, date):
    try:
        blacklist = Blacklist(favorite_id=favorite_id, vk_id=vk_id, name=name, surname=surname, date=date)
        Base.session.add(blacklist)
        Base.session.commit()
    except:
        Base.session.rollback()
