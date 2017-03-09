import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com']
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }

    def parse(self, response):
        for book_url in response.css('article.product_pod > h3 > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book)

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book(self, response):
        yield {
            'title': response.css('.product_main h1::text').extract_first(),
            'price': float(response.css('.product_main p.price_color::text').re_first('£(.*)')),
            'stock': int(
                ''.join(
                    response.css('.product_main .instock.availability ::text').re('(\d+)')
                )
            ),
        }
