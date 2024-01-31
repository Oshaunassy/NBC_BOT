import os

from aiogram import types, Dispatcher
from config import bot
from database.db import Database
from keyboards import inline_buttons
from aiogram.utils.deep_linking import _create_link
import binascii
from const import REFERENCE_MENU_TEXT


async def reference_menu_call(call: types.CallbackQuery):
    datab = Database()
    data = datab.sql_select_referral_menu_info(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_MENU_TEXT.format(
            users=call.from_user.first_name,
            balance=data['balance'],
            total=data['total_referrals']
        ),
        reply_markup=await inline_buttons.referral_keyboard()
    )


async def my_referrals(call: types.CallbackQuery):
    datab = Database()
    my_referrals = datab.sql_select_referral_menu_info(
        owner=call.from_user.id
    )
    list_referrals = ''
    for user in my_referrals:
        if isinstance(user, dict) and 'username' in user:
            list_referrals += (f"@{user['username']}\n\n")
            await bot.send_message(
                chat_id=call.from_user.id,
                text=list_referrals
                )


async def generate_link(call: types.CallbackQuery):
    datab = Database()
    users = datab.sql_select_user(tg_id=call.from_user.id)
    if users and isinstance(users, list) and len(users) > 0:
        user = users[0]
        if not user["link"]:
            token = binascii.hexlify(os.urandom(8)).decode()
            link = await _create_link("start", payload=token)
            print(link)
            datab.sql_update_link(
                link=link,
                tg_id=call.from_user.id,
                )
            await bot.send_message(
                chat_id=call.from_user.id,
                text=f"Here's your new link:{link}",
                )
        else:
             await bot.send_message(
                chat_id=call.from_user.id,
                text=f"Here's your old link:{user['link']}",
                )


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu_call, lambda call: call.data == 'reference_menu')
    dp.register_callback_query_handler(generate_link, lambda call: call.data == 'generate_link')
    dp.register_callback_query_handler(my_referrals, lambda call: call.data == 'my_referrals')
