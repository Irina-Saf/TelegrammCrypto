from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase
# from core.db import Base


# metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=True)
    username = Column(String(25), nullable=False)
    telegram_id = Column(Integer, unique=True)
    language_code = Column(String(5), nullable=False)
    is_premium = Column(Boolean, default=False)
    # added_to_attachment_menu=None,
    # can_join_groups=None,
    # can_read_all_group_messages=None,
    # supports_inline_queries=None)")


users = User.__table__
