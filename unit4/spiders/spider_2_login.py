import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes-loginspider-v1'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css("input[name=csrf_token] ::attr(value)").extract_first()
        yield scrapy.FormRequest(
            response.url,
            formdata={
                'csrf_token': token,
                'username': 'valdir',
                'password': 'abc'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        for quote in response.css('.quote'):
            yield {
                'text': quote.css('span::text').extract_first(),
                'author_name': quote.css('small.author::text').extract_first(),
                'author_url': response.urljoin(quote.css('small.author + a::attr(href)').extract_first()),
                'author_goodreads_url': quote.css(
                    'small.author ~ a[href*="goodreads.com"]::attr(href)'
                ).extract_first(),
                'tags': quote.css('.tags a::text').extract(),
            }
