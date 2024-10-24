from pathlib import Path


def format(path: Path, *args) -> Path:
    formatted_path = str(path).format(*args)
    return Path(formatted_path)


def create_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def create_file(content: bytes, path: Path) -> None:
    with open(path, 'wb') as buffer:
        buffer.write(content)
