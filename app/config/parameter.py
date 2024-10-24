from os import environ
from . import path


SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.DATABASE_FILE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WEBSOCKET_MAX_MESSAGE_SIZE = 1024 * 1024 * 8

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(' ')

JSON_SORT_KEYS = False
