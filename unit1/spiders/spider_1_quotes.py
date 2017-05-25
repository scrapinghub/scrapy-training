import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes1"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        requests = []
        for url in urls:
            requests.append(scrapy.Request(url=url, callback=self.parse))
        return requests

    def parse(self, response):
        self.log('I just visited {}'.format(response.url))
