import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons


async def nbc_start_button(message: types.Message):
    datab = db.Database()
    # try:
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    # except sqlite3.IntegrityError:
    #     pass
    print(message)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello, {message.from_user.first_name}",
        reply_markup=await inline_buttons.nbc_start_keyboard()
    )
def register_nbc_start_handlers(dp: Dispatcher):
    dp.register_message_handler(nbc_start_button, commands=['start'])