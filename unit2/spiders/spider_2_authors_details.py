import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'authors-details'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for href in response.css('.author + a::attr(href)').extract():
            yield scrapy.Request(
                response.urljoin(href),
                callback=self.parse_author_page
            )

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author_page(self, response):
        yield {
            'name': response.css('h3.author-title::text').extract_first(default='').strip(),
            'birth_date': response.css('.author-born-date::text').extract_first(),
            'birth_place': response.css('.author-born-location::text').re_first('in (.*)'),
        }
