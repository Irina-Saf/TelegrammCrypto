from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from utils import create_user, delete_all_user
import keyboards as kb

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("create_user"))
async def test_handler(msg: Message):
    text = create_user(msg.from_user)
    await msg.reply(text)


@router.message(Command("delete_all_user"))
async def del_all_user(msg: Message):
    text = delete_all_user()
    await msg.reply(str(text))


# @router.message(Command("help"))
# async def help_handler(msg: Message):
#     await msg.reply("Привет!\nНапиши мне что-нибудь!")


@router.message(Command("test"))
async def test_handler(msg: Message):
    # text = create_user(msg.from_user)
    await msg.reply("OLOLOLOL")
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
