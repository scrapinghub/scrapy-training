import scrapy


class BooksNoItemLoaderSpider(scrapy.Spider):
    name = 'books-no-itemloader'
    start_urls = [
        'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'http://books.toscrape.com/catalogue/soumission_998/index.html',
        'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
    ]
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }

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
