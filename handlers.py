from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Доров бля, що хоч?")

@router.message(F.text == "Меню")
@router.message(F.text == "Давай назад в меню нахооой")
@router.message(F.text == "️◀️ Давай назад в меню нахооой")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)