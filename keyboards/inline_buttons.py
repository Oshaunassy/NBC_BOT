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
    registration_button = InlineKeyboardButton(
        "Start Registration",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="view_profile"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(view_profile_button)
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

async def like_dislike_keyboard(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like",
        callback_data=f"like_{owner}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike",
        callback_data="view_profile"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update",
        callback_data='update_profile'
    )
    dislike_button = InlineKeyboardButton(
        "Delete",
        callback_data='delete_profile'
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

