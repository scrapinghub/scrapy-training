import scrapy
import js2xml


class QuotesJs2XmlSpider(scrapy.Spider):
    name = 'quotes-js2xml'
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        script = response.xpath('//script[contains(., "var data =")]/text()').extract_first()
        sel = scrapy.Selector(root=js2xml.parse(script))

        for quote in sel.css('var[name="data"] > array > object'):
            yield {
                'text': quote.css('property[name="text"] > string::text').extract_first(),
                'author': quote.css('property[name="author"] property[name="name"] > string::text').extract_first(),
                'tags': quote.css('property[name="tags"] string::text').extract(),
            }

        link_next = response.css('li.next a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))
