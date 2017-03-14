import scrapy
from selenium import webdriver


class QuotesJsSpider(scrapy.Spider):
    name = 'quotes-js'
    start_urls = [
        'http://quotes.toscrape.com/js'
    ]

    def __init__(self, *args, **kwargs):
        # phantomjs binary must be somewhere in your PATH
        self.driver = webdriver.PhantomJS()
        super(QuotesJsSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)
        for quote in sel.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_page = sel.css('li.next > a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
