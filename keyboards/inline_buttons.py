from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def nbc_start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 💥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python",
        callback_data="python"
    )

    mojo_button = InlineKeyboardButton(
        "Mojo",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup
