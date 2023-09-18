from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types
from utils import user_exists


def base_kb(data):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Меню")
    )
    if not user_exists(data):
        builder.row(
            types.KeyboardButton(text="Зарегистрироваться", request_contact=True))
    return builder.as_markup(resize_keyboard=True)