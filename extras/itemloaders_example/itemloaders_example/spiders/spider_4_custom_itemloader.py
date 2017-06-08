import scrapy
from itemloaders_example.items import QuoteItem
from itemloaders_example.itemloaders import QuoteLoader


class QuotesCustomItemLoaderSpider(scrapy.Spider):
    name = "quotes-custom-itemloader"
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # have a look at the itemloaders.py file to see how we've defined
            # the input and output processors for the QuoteLoader class.
            il = QuoteLoader(item=QuoteItem(), selector=quote)
            il.add_css('text', 'span.text::text')
            il.add_css('author_name', 'small.author::text')
            il.add_css('tags', 'a.tag::text')
            il.add_value('url', response.url)
            yield il.load_item()

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
