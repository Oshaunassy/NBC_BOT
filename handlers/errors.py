import asyncio
import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils import exceptions
from config import bot

async def exception_retry_handler(update: types.Update, exception: exceptions.RetryAfter):
    await asyncio.sleep(exception.timeout)
    return True

def register_error_handlers(dp:Dispatcher):
    dp.register_errors_handler(
        exception_retry_handler,
        exception=exceptions.RetryAfter
    )