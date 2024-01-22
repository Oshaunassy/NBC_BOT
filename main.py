from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    registration,
    profile,
)

from database import db

async def on_startup(_):
    datab = db.Database()
    datab.sql_create_tables()


start.register_nbc_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
# profile.register_profile_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
