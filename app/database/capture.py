from datetime import datetime
from flask_sqlalchemy.model import Model
from sqlalchemy import Column, DateTime, Integer, String
from typing import Dict, List

from app.extension import database


Captures = List['Capture']


class Capture(database.Model, Model):
    __tablename__ = 'capture'

    id = Column(Integer, autoincrement=True, primary_key=True)
    file_name = Column(String(40), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def save(capture: 'Capture') -> None:
        try:
            database.session.add(capture)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def find_all(cls) -> Captures:
        return cls.query.all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Capture':
        return cls.query.filter_by(id=id).first()

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def to_dict(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'file_name': self.file_name,
            'created_at': self.created_at
        }
