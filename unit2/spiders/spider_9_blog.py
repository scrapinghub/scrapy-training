import scrapy


class BlogCrawler(scrapy.Spider):
    name = 'blog'
    start_urls = ['http://blog.scrapinghub.com']

    def parse(self, response):
        for post_url in response.css('h2.entry-title > a::attr(href)').extract():
            yield scrapy.Request(url=post_url, callback=self.parse_post)

        next_page_url = response.css('div.prev-post > a::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_post(self, response):
        tags = response.css('div.tags a::text').extract()
        if tags:
            yield {
                'url': response.url,
                'title': response.css('h1.entry-title::text').extract_first(),
                'author': response.css('span.author > a::text').extract_first(),
                'date': response.css('time.entry-date::attr(datetime)').extract_first(),
                'tags': tags,
            }
