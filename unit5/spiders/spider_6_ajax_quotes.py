import json
import scrapy


class SpidyQuotesScroll(scrapy.Spider):
    name = 'scroll'
    base_url = 'http://quotes.toscrape.com/api/quotes?page=%d'
    start_urls = [base_url % 1]

    def parse(self, response):
        # extract data from response
        json_data = json.loads(response.text)
        for quote in json_data['quotes']:
            yield quote
        if json_data['has_next']:
            yield scrapy.Request(self.base_url % (int(json_data['page']) + 1))
