import httpx
import asyncio
from parsel import Selector

class AsyncNewScraper:
    START_URL = "https://rezka.ag/"
    URL = "https://rezka.ag/page/9/"
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    # def __init__(self):
    #     self.response = requests.get(self.URL, headers=self.HEADERS).text
    # print(response.text)

    LINK_XPATH = '//div[@class="b-content__inline_item"]'
    IMAGE_XPATH = '//div[@class="b-content__inline_item-cover"]/a[@href="https://rezka.ag/films/melodrama/61645-velikaya-ironiya-2023.html"]/img'

    async def async_generator(self,limit):
        for page in range(1, limit + 1):
            yield page

    async def get_pages(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            async for page in self.async_generator(limit=3):
                await self.get_url(client, self.START_URL.format(page=page))

            # await self.gather(*tasks)
    #         client=client,
    #         url=self.URL.format(
    #             page=page
    #         )
    #     )
    #     return data

    async def get_url(self, client, url):
        response = await client.get(url)
        print('response-url: ', response.url)

        await self.scrape_url(response=response)

    async def scrape_url(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print(link)
if __name__ == "__main__":
    scraper = AsyncNewScraper()
    asyncio.run(scraper.get_pages())