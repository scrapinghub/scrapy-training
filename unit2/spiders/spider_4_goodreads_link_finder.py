import scrapy
from urllib import parse


class GoodreadsLinkFinderSpider(scrapy.Spider):
    name = 'goodreads-link-finder'
    allowed_domains = ['goodreads.com']
    start_urls = [
        'https://www.goodreads.com/',
    ]

    def urls_from(self, response):
        def is_absolute_url(url):
            return bool(parse.urlparse(url).netloc)

        for url in response.css('a[href]::attr(href)').extract():
            if not is_absolute_url(url):
                url = response.urljoin(url)
            yield url

    def parse(self, response):
        for url in self.urls_from(response):
            if '/book/show/' in url:
                yield scrapy.Request(url, callback=self.parse_book_page)
            elif '/genres/' in url or '/list/show/' in url:
                yield scrapy.Request(url, callback=self.parse)

        next_page = response.css('a.next_page[href*=\/show]::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        yield {
            'title': response.css('h1.bookTitle::text').extract_first(default='').strip(),
            'authors': response.css('div#bookAuthors a.authorName ::text').extract(),
            'rating': response.css('div#bookMeta span.average ::text').extract_first(),
        }
        self.parse(response)
