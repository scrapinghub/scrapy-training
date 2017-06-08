import scrapy


# this is just a regular spider generating schema-less dictionaries
class QuotesNoItemLoaderSpider(scrapy.Spider):
    name = "quotes-no-item"
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author_name': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
                'url': response.url,
            }

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
