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
    # added_to_attachment_menu=None,
    # can_join_groups=None,
    # can_read_all_group_messages=None,
    # supports_inline_queries=None)")


users = Tg_User.__table__
