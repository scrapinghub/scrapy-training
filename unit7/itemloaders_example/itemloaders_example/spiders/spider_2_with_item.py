import scrapy


# the items are generally defined in the project's items.py, not here
class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author_name = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()


# this spider generates items following the schema defined above
class QuotesWithItemSpider(scrapy.Spider):
    name = "quotes-with-item"
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author_name'] = quote.css('span small::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            item['url'] = response.url
            yield item

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
