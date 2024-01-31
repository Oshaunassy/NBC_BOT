import requests
from parsel import Selector

class AzattykCsraper:
    START_URL = "https://www.wildberries.ru/"
    URL = "https://static-basket-01.wbbasket.ru/vol1/crm-bnrs/adsf/1706713302988613834.jpg"
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    LINK_XPATH = '//a[contains(@class, "product-card__link") and contains(@class, "j-card-link") and contains(@class, "j-open-full-product-card")]/@href'

    def parse_data(self):
        text = requests.get(url=self.URL, headers=self.HEADERS).text


        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).getall()

        for link in links:
            print(self.START_URL + link)
            return links

if __name__ == "__main__":
    scraper = AzattykCsraper()
    scraper.parse_data()

