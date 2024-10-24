from base64 import b64decode
from pathlib import Path
from werkzeug.exceptions import NotFound
from uuid import uuid4

from app.config import path
from app.database import Capture, Captures
from app.facade import storage


# common _

def compose_file_path(file_name: str) -> Path:
    return storage.format(path.CAPTURE_FILE, file_name)


# 4event _

def generate_file_name() -> str:
    return f'{uuid4()}.png'


def store(base64: str, file_name: str) -> None:
    content = b64decode(base64)
    path = compose_file_path(file_name)
    storage.create_file(content, path)


def create(file_name: str) -> Capture:
    capture = Capture(file_name)
    Capture.save(capture)
    return capture


# 4route _

def get_all() -> Captures:
    return Capture.find_all()


def get_one_by_id(id: int) -> Capture:
    capture = Capture.find_first_by_id(id)
    if not capture: raise NotFound('Capture not found.')
    return capture
