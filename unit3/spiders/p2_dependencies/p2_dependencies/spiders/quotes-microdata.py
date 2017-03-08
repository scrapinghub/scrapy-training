import scrapy
from extruct.w3cmicrodata import MicrodataExtractor


class QuotesMicrodataSpider(scrapy.Spider):
    name = "quotes-microdata"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        extractor = MicrodataExtractor()
        items = extractor.extract(response.text, response.url)['items']
        for it in items:
            yield it['properties']

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
