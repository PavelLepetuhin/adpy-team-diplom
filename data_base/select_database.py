
from sqlalchemy.orm import sessionmaker

# from create_database import Favourite, BotUsers, Top3Photo, Blacklist
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from settings import USER, PASSWORD, HOST, DB_NAME


# Создание подключения к базе данных
connection_string = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(connection_string)
Base = declarative_base()


def select_favorite(favorite):
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[favorite]
    result = session.query(table).all()
    return result


def select_blacklist(blacklist):
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[blacklist]
    result = session.query(table).all()
    return result