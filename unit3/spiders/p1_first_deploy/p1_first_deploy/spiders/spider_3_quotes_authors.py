import scrapy


class QuotesAuthorsSpider(scrapy.Spider):
    name = 'quotes-authors'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = {
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            author_url = quote.css('.author + a::attr(href)').extract_first()
            yield scrapy.Request(
                response.urljoin(author_url),
                meta={'item': item},
                dont_filter=True,
                callback=self.parse_author_page
            )

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author_page(self, response):
        item = response.meta.get('item', {})
        item['author'] = {
            'name': response.css('h3.author-title::text').extract_first(default='').strip(),
            'birth_date': response.css('.author-born-date::text').extract_first(default='').strip(),
            'birth_place': response.css('.author-born-location::text').extract_first(default='').strip(),
        }
        yield item
