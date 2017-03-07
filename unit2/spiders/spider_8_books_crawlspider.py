from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksCrawlSpider(CrawlSpider):
    name = 'books-crawlspider'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com']
    rules = [
        Rule(
            LinkExtractor(allow=('/catalogue/page-\d+.html')),
            follow=True
        ),
        Rule(
            LinkExtractor(deny=('/category/books', '/catalogue/page-\d+.html', '.com/index.html')),
            callback='parse_book_page',
            follow=True
        ),
    ]

    def parse_book_page(self, response):
        yield {
            'title': response.css('.product_main h1::text').extract_first(),
            'price': response.css('.product_main p.price_color::text').re_first('£(.*)'),
            'stock': int(
                ''.join(
                    response.css('.product_main .instock.availability ::text').re('(\d+)')
                )
            ),
        }
