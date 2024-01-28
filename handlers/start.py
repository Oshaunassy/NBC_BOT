import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot, MEDIA_DESTINATION
from database import db
from const import START_MENU
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
    print(message.get_full_command())
    command = message.get_full_command()

    if command[1] != "":
        link = await _create_link('start', payload=command[1])
        owner = datab.sql_select_user_by_link(
            link=link,
        )
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="You can't use own link!"
            )
            return
        try:
            datab.sql_insert_referral(
                username=message.from_user.username,
                owner=owner['telegram_id'],
                referral=message.from_user.id
            )
            datab.sql_update_balance(
                owner=owner['telegram_id']
            )
        except sqlite3.IntegrityError:
            pass

    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=f"Hello, {message.from_user.first_name}",
    #     reply_markup=await inline_buttons.nbc_start_keyboard()
    # )
    with open(MEDIA_DESTINATION + "bot_pic.png", 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_buttons.nbc_start_keyboard()
        )
    #
    # with open(MEDIA_DESTINATION + "bot_ani.gif") as animation:
    #     await bot.send_animation(
    #         chat_id=message.from_user.id,
    #         animation=animation,
    #         caption=START_MENU.format(
    #             name=message.from_user.first_name
    #         ),
    #         reply_markup=await inline_buttons.nbc_start_keyboard()
    #     )



def register_nbc_start_handlers(dp: Dispatcher):
    dp.register_message_handler(nbc_start_button, commands=['start'])
