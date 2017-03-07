from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GoodreadsCrawlSpider(CrawlSpider):
    name = 'goodreads-crawlspider'
    allowed_domains = ['goodreads.com']
    start_urls = ['http://www.goodreads.com']
    rules = [
        Rule(
            LinkExtractor(allow=('/genres/', '/list/show/')),
            follow=True
        ),
        Rule(
            LinkExtractor(allow=('/book/show/')),
            callback='parse_book_page',
            follow=True
        ),
    ]

    def parse_book_page(self, response):
        yield {
            'title': response.css('h1.bookTitle::text').extract_first(default='').strip(),
            'authors': response.css('div#bookAuthors a.authorName ::text').extract(),
            'rating': response.css('div#bookMeta span.average ::text').extract_first(),
        }
