from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

from lib_chess.models.base import Base
import uuid


def _init_uuid():
    return str(uuid.uuid4())

# 3. Define a table as a Python class
class Game(Base):
    __tablename__ = 'game'

    # id = Column(Integer, primary_key=True, autoincrement=True)

    uuid = Column(String, primary_key=True, default=_init_uuid)

    # serialized string of game state
    fen = Column(String)

    # def __repr__(self):
    #     return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"