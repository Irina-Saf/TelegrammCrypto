from sqlalchemy.orm import Session
from models import Tg_User
from db import engine


def create_user(data):
    with Session(autoflush=False, bind=engine) as db:
        if user_exists(data):
            result = f'Пользователь с id {data.from_user.id} уже существует'
        else:
            str_phone = (data.contact.phone_number).replace('+', '')
            new_user = Tg_User(
                first_name=data.from_user.first_name,
                last_name=data.from_user.last_name,
                username=data.from_user.username,
                telegram_id=data.from_user.id,
                phone_number=int(str_phone),
                is_premium=data.from_user.is_premium is not None
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            result = f'Пользователь {data.from_user.username} добавлен успешно'

        return result


def delete_all_user():
    with Session(autoflush=False, bind=engine) as db:

        all_users = db.query(Tg_User).all()
        mess_print = f'Было удалено пользователей - [{len(all_users)}]\n'
        for one_user in all_users:
            db.delete(one_user)
            mess = f'{one_user.username}, tg ID {one_user.telegram_id}\n'
            mess_print += mess
            # mess_print += f'{one_user.username}, tg ID {one_user.telegram_id}\n'
        db.commit()
        return mess_print


def user_exists(data):
    with Session(autoflush=False, bind=engine) as db:
        user_exists = db.query(db.query(Tg_User).filter_by(
            telegram_id=data.from_user.id).exists()).scalar()
        return user_exists
