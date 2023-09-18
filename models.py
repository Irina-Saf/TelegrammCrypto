from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase
# from core.db import Base


# metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Tg_User(Base):
    __tablename__ = "Tg_User"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=True)
    username = Column(String(30), nullable=False)
    telegram_id = Column(Integer, unique=True)
    phone_number = Column(Integer, nullable=True)
    is_premium = Column(Boolean, default=False)


users = Tg_User.__table__
