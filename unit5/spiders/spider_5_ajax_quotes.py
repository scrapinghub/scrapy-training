import json
import scrapy


class QuotesScroll(scrapy.Spider):
    name = 'quotes-scroll'
    base_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [base_url.format(1)]

    def parse(self, response):
        # extract data from response
        json_data = json.loads(response.text)
        for quote in json_data['quotes']:
            yield quote
        if json_data['has_next']:
            yield scrapy.Request(
                self.base_url.format((int(json_data['page']) + 1))
            )
