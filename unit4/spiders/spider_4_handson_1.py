import scrapy


class HNewsLoginSpider(scrapy.Spider):
    name = 'hnews'
    start_urls = ['https://news.ycombinator.com/login?goto=news']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formnumber=0,
            formdata={'acct': 'scrape1123', 'pw': 'scrape1123'},
            callback=self.parse_homepage
        )

    def parse_homepage(self, response):
        yield {
            'username': response.css('span.pagetop a[href^="user"] ::text').extract_first(),
            'points': response.css(
                'td[style*="text-align:right"] > span.pagetop'
            ).re_first('\((\d+)\)'),
        }
