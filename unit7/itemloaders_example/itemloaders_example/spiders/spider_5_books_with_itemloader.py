import scrapy
from scrapy.loader import ItemLoader
from itemloaders_example.items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'http://books.toscrape.com/catalogue/soumission_998/index.html',
        'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
    ]

    def parse(self, response):
        il = ItemLoader(item=BookItem(), response=response)
        il.add_css('title', '.product_main h1::text')
        il.add_css('rating', 'p.star-rating::attr(class)')
        il.add_css('price', '.product_main p.price_color::text')
        il.add_css('stock', '.product_main .instock.availability ::text')
        il.add_css('category', 'ul.breadcrumb li:nth-last-child(2) ::text')
        return il.load_item()
