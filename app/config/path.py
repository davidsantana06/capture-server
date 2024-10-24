from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

STORAGE_DIR = ROOT_DIR / 'storage'
''' /storage/ '''

DATABASE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''

UPLOADS_DIR = STORAGE_DIR / 'uploads'
''' /storage/uploads/ '''

CAPTURE_FILE = UPLOADS_DIR / '{}'
''' /storage/uploads/*file_name* '''
