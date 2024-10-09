from dotenv import load_dotenv
from flask import Flask

from app.extensions import cors, socket_io
from app.facades import storage

from . import parameters
from . import paths


def _apply_parameters(app: Flask) -> None:
    app.json.sort_keys = parameters.JSON_SORT_KEYS
    for key in dir(parameters):
        is_parameter = key.isupper()
        if is_parameter:
            value = getattr(parameters, key)
            app.config[key] = value


def _create_uploads_dir() -> None:
    storage.create_dir(paths.UPLOADS_DIR)


def configure_enviroment(app: Flask) -> None:
    load_dotenv(paths.ENV_FILE)
    _apply_parameters(app)
    _create_uploads_dir()


def _configure_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameters.ALLOWED_HOSTS)


def _configure_socket_io(app: Flask) -> None:
    socket_io.init_app(
        app,
        cors_allowed_origins=parameters.ALLOWED_HOSTS,
        websocket_max_message_size=parameters.WEBSOCKET_MAX_MESSAGE_SIZE
    )


def configure_extensions(app: Flask) -> None:
    _configure_cors(app)
    _configure_socket_io(app)