from base64 import b64decode
from pathlib import Path
from uuid import uuid4

from app.config import paths
from app.database import Capture
from app.facades import storage


# common _

def compose_file_path(file_name: str) -> Path:
    return storage.format(paths.CAPTURE_FILE, file_name)


# for events _

def generate_file_name() -> str:
    return f'{uuid4()}.png'


def store(file_name: str, base64: str) -> None:
    path = compose_file_path(file_name)
    content = b64decode(base64)
    storage.create_file(path, content)


def create(file_name: str) -> Capture:
    capture = Capture(file_name)
    Capture.save(capture)
    return capture
