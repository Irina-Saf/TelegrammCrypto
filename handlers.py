from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import keyboards as kb

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("test"))
async def test_handler(msg: Message):
    await msg.reply("Привет!\nНапиши мне что-нибудь!")

# @router.message(Command("help"))
# async def help_handler(msg: Message):
#     await msg.reply("Привет!\nНапиши мне что-нибудь!")

# @router.message() or router.message(Command("help"))
@router.message() 
async def test_handler(msg: Message):
    kb = [
        [
            types.KeyboardButton(text="Кнопка 1"),
            types.KeyboardButton(text="Кнопка 2")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await msg.answer("Меню", reply_markup=keyboard)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
