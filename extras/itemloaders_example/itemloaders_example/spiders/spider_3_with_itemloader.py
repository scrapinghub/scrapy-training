import scrapy
from scrapy.loader import ItemLoader
from itemloaders_example.items import QuoteItem


class QuotesWithItemLoaderSpider(scrapy.Spider):
    name = "quotes-with-itemloader"
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # check the items.QuoteItem class to see how we've defined
            # the input and output processors for each one of these fields
            il = ItemLoader(item=QuoteItem(), selector=quote)
            il.add_css('text', 'span.text::text')
            il.add_css('author_name', 'small.author::text')
            il.add_css('tags', 'a.tag::text')
            il.add_value('url', response.url)
            yield il.load_item()

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
