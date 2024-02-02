import requests
from parsel import Selector

class RezkaScraper:
    START_URL = "https://rezka.ag/"
    URL = "https://rezka.ag/page/9/"
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    response = requests.request("GET", URL, headers=HEADERS)
    print(response.text)

    LINK_XPATH = '//div[@class="b-content__inline_item"]'

    def parse_data(self):
        response = requests.get(self.URL, headers=self.HEADERS).text
        tree = Selector(text=response)
        items = tree.xpath(self.LINK_XPATH)
        url = []
        for item in items:
            film_url = item.xpath('.//a[@href]').xpath('./@href').get()
            url.append(film_url)
            return url



if __name__ == "__main__":
    scraper = RezkaScraper()
    scraper.parse_data()

