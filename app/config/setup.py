from dotenv import load_dotenv
from flask import Flask

from app.database import *
from app.extension import cors, database, socket_io
from app.facade import storage

from . import parameter
from . import path


def _apply_parameters(app: Flask) -> None:
    app.json.sort_keys = parameter.JSON_SORT_KEYS
    for key in dir(parameter):
        is_parameter = key.isupper()
        if is_parameter:
            value = getattr(parameter, key)
            app.config[key] = value


def _create_uploads_dir() -> None:
    storage.create_dir(path.UPLOADS_DIR)


def setup_enviroment(app: Flask) -> None:
    load_dotenv(path.ENV_FILE)
    _apply_parameters(app)
    _create_uploads_dir()


def _setup_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _setup_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameter.ALLOWED_HOSTS)


def _setup_socket_io(app: Flask) -> None:
    socket_io.init_app(
        app,
        cors_allowed_origins=parameter.ALLOWED_HOSTS,
        websocket_max_message_size=parameter.WEBSOCKET_MAX_MESSAGE_SIZE
    )


def setup_extensions(app: Flask) -> None:
    _setup_database(app)
    _setup_cors(app)
    _setup_socket_io(app)
