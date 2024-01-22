import re
import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.db import Database
from const import PROFILE_TEXT
from keyboards import inline_buttons
import random

async def my_profile_call(call: types.CallbackQuery):
    datab = Database()
    profile = datab.sql_select_profile(
        tg_id=call.from_user.id
    )
    print(profile)
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['bio'],
                    age=profile['age'],
                    sign=profile['sign'],
                ),
                reply_markup=await inline_buttons.my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="you didn't registered,"
                "please register to view your profile"
        )
    async def random_filter_profile_call(call: types.CallbackQuery):
        datab = Database()
        profile = datab.sql_select_all_profiles(owner=call.from_user.id)
        if not profile:
            await bot.send_message(
                chat_id=call.from_user.id,
                text="you've liked all profiles, come back later"
            )
            return

        random_profile = random.choice(profiles)
        with open(random_profile["photo"], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=random_profile['nickname'],
                    bio=random_profile['bio'],
                    age=random_profile['age'],
                    sign=random_profile['sign'],
                ),
                reply_markup=await inline_buttons.like_dislike_keyboard(
                    owner=random_profile['telegram_id'])
            )

async def detect_like_profiles_call(call: types.CallbackQuery):
    datab = Database()
    owner = re.sub('like_', "", call.data)
    print(call.data)
    print(owner)
    try:
        datab.sql_insert_like(
            owner=owner,
            liker=call.from_user.id,
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="you've liked this profile!"
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)


    def register_profile_handlers(dp:Dispatcher):
        dp.register_callback_query_handler(
            my_profile_call,
            lambda call: call.data == "my_profile"
        )
        dp.register_callback_query_handler(
            random_filter_profile_call,
            lambda call: call.data == "view_profiles"
        )
        dp.register_callback_query_handler(
            detect_like_profiles_call,
            lambda call: "like_" in call.data
        )

