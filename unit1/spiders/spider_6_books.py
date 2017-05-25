import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }

    def start_requests(self):
        for url in open('urls.txt'):
            yield scrapy.Request(url.strip())

    def parse(self, response):
        rating = response.css('p.star-rating::attr(class)').extract_first().split(' ')[-1]
        yield {
            'rating': self.ratings_map.get(rating.lower(), ''),
            'title': response.css('.product_main h1::text').extract_first(),
            'price': response.css('.product_main p.price_color::text').re_first('£(.*)'),
            'stock': int(
                ''.join(
                    response.css('.product_main .instock.availability ::text').re('(\d+)')
                )
            ),
            'category': ''.join(
                response.css('ul.breadcrumb li:nth-last-child(2) ::text').extract()
            ).strip(),
        }
