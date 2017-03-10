import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes-loginspider-v2'
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'any', 'password': 'doesntmatter'},
            callback=self.after_login,
        )

    def after_login(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span::text').extract_first(),
                'author_name': quote.css('small.author::text').extract_first(),
                'author_goodreads_url': quote.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first(),
                'tags': quote.css('.tags a::text').extract()
            }
