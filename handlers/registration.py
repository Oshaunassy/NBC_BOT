import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from const import START_MENU, PROFILE_TEXT
from database import db
from database.db import Database
from keyboards import inline_buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    favorite_actor = State()
    favorite_genre = State()
    photo = State()

async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="send me your nickname, pls!"
    )
    await RegistrationStates.nickname.set()

async def load_nickname(message:types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="send me your bio"
    )
    await RegistrationStates.next()

async def load_biography(message:types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="how old are you?\n"
                "(Only numeric age in text)\n"
                "example: 25, 30"
    )
    await RegistrationStates.next()

async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told you send me Only numeric text\n"
                 "registration failed\n"
                 "Restart registration!!!"
        )
        await state.finish()
        return


    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="what is your zodiac sign?"
    )
    await RegistrationStates.next()

async def load_zodiac_sign(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="send me your favorite actor"
    )
    await RegistrationStates.next()

async def load_favorite_actor(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['favorite_actor'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="send me your favorite genre"
    )
    await RegistrationStates.next()

async def load_favorite_genre(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['favorite_genre'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="send me your photo\n"
             "(only in photo mode sender)"
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            sign=data['sign'],
            favorite_actor=data['favorite_actor'],
            favorite_genre=data['favorite_genre'],
            photo=path.name,
        )

        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    sign=data['sign'],
                    favorite_actor=data['favorite_actor'],
                    favorite_genre=data['favorite_genre'],
                ),
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text='You have successfully Registered\n'
                 'Congratulation'
        )

def register_registration_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == 'registration'
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_favorite_actor,
        state=RegistrationStates.favorite_actor,
        content_types=['text']
    )
    dp.register_message_handler(
        load_favorite_genre,
        state=RegistrationStates.favorite_genre,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentType.PHOTO
    )
