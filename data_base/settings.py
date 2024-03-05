# create a module "settings.py"
import os


USER = os.getenv('username_DB')
PASSWORD = os.getenv('password_DB')
HOST = os.getenv('localhost_DB')
DB_NAME = os.getenv('name_DB')
