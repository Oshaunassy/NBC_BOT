import requests
from parsel.selector import Selector

class AzattykCsraper:
    START_URL = "https://www.azattyk.org"
    URL = "https://www.azattyk.org"
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \n'
                     '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\n'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    LINK_XPATH = '//a[@class=media-block]/@href'

    def parse_data(self):
        text = requests.get(url=self.URL, headers=self.HEADERS).text
        print(text)

        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).getall()

        for link in links:
            print(self.START_URL + link)
            return links

if __name__ == "__main__":
    scraper = AzattykCsraper()
    scraper.parse_data()

