import httpx
import asyncio
from parsel import Selector
from database.db import Database


class AsyncNewScraper:
    START_URL = "https://rezka.ag/"
    URL = "https://rezka.ag/page/9/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    # def __init__(self):
    #     self.response = requests.get(self.URL, headers=self.HEADERS).text
    # print(response.text)

    LINK_XPATH = '//div[@class="b-content__inline_item-link"]/a/@href'
    IMAGE_XPATH = '//div[@class="b-content__inline_item-cover"]/a/img/@src'

    async def async_generator(self,limit):
        for page in range(1, limit + 1):
            yield page

    async def get_pages(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            async for page in self.async_generator(limit=5):
                data = await self.get_url(
                    client=client,
                    url=self.URL.format(
                        page=page))

    async def get_url(self, client, url):
        response = await client.get(url=url)
        # print('response-url: ', response.url)

        await self.scrape_url(response=response)

    async def scrape_url(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        images = tree.xpath(self.IMAGE_XPATH).getall()
        datab = Database()
        for i in range(6):
            datab.sql_insert_film(links[i], images[i])


    # async def async_data(self,limit):
    #     for data in range(1, limit + 1):
    #         yield data
    #
    # async def get_data(self):
    #     async with httpx.AsyncClient(headers=self.HEADERS) as client:
    #         async for data in self.async_generator(limit=5):
    #             await self.get_url(client, self.START_URL.format(data=data))
    #         print(f"DATA:{data}")


if __name__ == "__main__":
    scraper = AsyncNewScraper()
    asyncio.run(scraper.get_pages())
    # asyncio.run(scraper.get_data())

