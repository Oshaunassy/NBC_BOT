from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons

async def nbc_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo? ",
        reply_markup=await inline_buttons.questionnaire_first_answers()
    )

async def python_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool you are awesome python developer",
        reply_markup=await inline_buttons.questionnaire_first_answers()
    )

async def mojo_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="don't lie. Mojo is in alpha version.",
        reply_markup=await inline_buttons.questionnaire_first_answers()
    )

def register_questionnaire_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(nbc_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_answers,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_answers,
                                       lambda call: call.data == "mojo")