from aiogram import types,Dispatcher
from scraping.async_scraper import AsyncNewScraper
from database.db import Database

async def get_films(call: types.CallbackQuery):
    datab = Database()
    scraper = AsyncNewScraper()
    await scraper.get_pages()
    films = datab.sql_select_film()
    # datab.drop_film()
    for i in films[:5]:
        await call.message.answer_photo(i['image'], caption=i['url'])

def register_get_data(dp:Dispatcher):
    dp.register_callback_query_handler(get_films, lambda call: call.data=='choose_the_data')