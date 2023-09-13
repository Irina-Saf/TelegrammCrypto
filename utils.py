from sqlalchemy.orm import Session
# from sqlalchemy.sql import exists
from models import User
# import fastapi
from db import engine


def create_user(data):
    with Session(autoflush=False, bind=engine) as db:
        # serch_user = db.query(User).filter(
        #     User.telegram_id == data.id)
        # serch_user = db.query(serch_user.exists())
        user_exists = db.query(db.query(User).filter_by(
            telegram_id=data.id).exists()).scalar()
        if user_exists:
            result = f'Пользователь с id {data.id} уже существует'
        else:
            new_user = User(
                first_name=data.first_name,
                last_name=data.last_name,
                username=data.username,
                telegram_id=data.id,
                language_code=data.language_code,
                is_premium=data.is_premium is not None
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            result = f'Пользователь {data.username} добавлен успешно'

        return result

# create_user(new_user)


# def test_get(id):
#     with Session(autoflush=False, bind=engine) as db:
#         # serch_user = db.query(User).filter(User.telegram_id == telegram_id)
#         # db.query(serch_user.exists())

#         # serch_user_get = db.get(User, 3)

#         serch_user = db.query(db.query(User).filter_by(telegram_id=id).exists()).scalar()
#         print(serch_user)


# test_get(911723)

# def test_none(test_premium):
#     is_premium = test_premium is not None
#     # return "default" if x is None else x
#     print(is_premium)


# test_none(None)


# with Session(autoflush=False, bind=engine) as db:
#     users = db.query(User).all()
#     for user in users:
#         print(
#             f'Ваш никнейм - {user.username}, Имя: {user.first_name}, Фамилия: {user.last_name}, id: {user.id}')


# with Session(autoflush=False, bind=engine) as db:
#     user = db.query(User).filter(User.id == 3).first()
#     if (user != None):
#         user.last_name = "Mikich"
#         db.commit()
#         user_new = db.query(User).filter(User.id == 3).first()
#         print(f'Ваша фамилия изменена на {user_new.last_name}')
#     else:
#         print('Такого юзера не существует')


# with Session(autoflush=False, bind=engine) as db:
#     user = db.query(User).filter(User.id == 5).first()
#     if user != None:
#         db.delete(user)
#         db.commit()
#         print('Пользователь удален успешно')
#     else:
#         print('Такого юзера не существует')


def delete_all_user():
    with Session(autoflush=False, bind=engine) as db:

        all_users = db.query(User).all()
        mess_print = f'Было удалено пользователей - [{len(all_users)}]\n'
        for one_user in all_users:
            db.delete(one_user)
            mess = f'{one_user.username}, tg ID {one_user.telegram_id}\n'
            mess_print += mess
            # Старайся не вводить лишние перменные
            # mess_print += f'{one_user.username}, tg ID {one_user.telegram_id}\n'
        db.commit()
        return mess_print

# delete_all_user()
