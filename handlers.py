from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from utils import create_user, delete_all_user
from keyboards import base_kb


router = Router()


@router.message(Command("test"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("create_user"))
async def test_handler(msg: Message):
    text = create_user(msg.from_user)
    await msg.reply(text)


@router.message(Command("delete_all_user"))
async def del_all_user(msg: Message):
    text = delete_all_user()
    await msg.reply(str(text), reply_markup=base_kb(msg))


# @router.message(Command("help"))
# async def help_handler(msg: Message):
#     await msg.reply("Привет!\nНапиши мне что-нибудь!")


@router.message(Command("start"))
async def test2_handler(msg: Message):
    await msg.reply("Выберите действие:", reply_markup=base_kb(msg))


@router.message(F.contact)
async def test_handler(msg: Message):
    text = create_user(msg)
    await msg.answer(text, reply_markup=base_kb(msg))


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
