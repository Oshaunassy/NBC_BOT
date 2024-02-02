from scraping import new_scraper
from aiogram import types, Dispatcher
from database.db import Database



async def get_film(call: types.CallbackQuery):
    datab = Database()
    films = datab.sql_select_film()
    if len(films) < 5:
        scraper = new_scraper.RezkaScraper()
        for i in scraper.parse_data()[:5]:
            datab.sql_insert_film(i)
            await call.message.answer(i)
        else:
            for i in films:
                await call.message.answer(i["url"])

def register_parsel_handlers(dp:Dispatcher):
    dp.register_message_handler(get_film, lambda call: call.data=='choose_the_film')