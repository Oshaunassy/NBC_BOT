import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import db
from const import BAN_USER_TEXT
from keyboards import inline_buttons

async def check_chat_message(message: types.message):
    datab = db.Database
    potential = datab.sql_select_ban_user(
        tg_id=message.from_user.id
    )
    print(potential)

    if potential:
        datab.sql_update_ban_count(
            tg_id=message.from_user.id
        )
        await bot.send_message(
            chat_id=message.chat.id,
            text=BAN_USER_TEXT.format(
                name=message.from_user.first_name,
                count=potential['count']
            )
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text="You didn't swear"
        )

def register_chat_actions_handlers(dp:Dispatcher):
    dp.register_message_handler(check_chat_message, commands=["ban_logic"])