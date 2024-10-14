from pathlib import Path


class StorageFacade():
    @property
    def current_working_dir(self) -> Path:
        return Path.cwd()

    def format(self, path: Path, *args) -> Path:
        formatted_path = str(path).format(*args)
        return Path(formatted_path)

    def create_dir(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)

    def create_file(self, content: bytes, path: Path) -> None:
        with open(path, 'wb') as buffer:
            buffer.write(content)
