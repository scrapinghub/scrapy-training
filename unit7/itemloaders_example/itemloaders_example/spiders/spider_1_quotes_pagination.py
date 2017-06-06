import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from itemloaders_example.items import Quote


class QuotesSpider(scrapy.Spider):
    name = "quotes-pagination"
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            il = ItemLoader(item=Quote(), selector=quote)
            il.add_css('text', 'span.text::text')
            il.add_css('author_name', 'small.author::text')
            il.add_css('tags', 'a.tag::text')
            il.add_value('ts', datetime.now())
            yield il.load_item()

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
