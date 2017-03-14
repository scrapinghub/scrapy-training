import json
import scrapy


class InfiniteScrollingSpider(scrapy.Spider):
    name = 'infinite-scrolling-pythonhelp'
    scrolling_url = 'https://pythonhelp.wordpress.com/?infinity=scrolling'

    def start_requests(self):
        yield scrapy.FormRequest(
            self.scrolling_url, formdata={'action': 'infinite_scroll', 'page': '1', 'order': 'DESC'},
            callback=self.parse_page, meta={'page': 1}
        )

    def parse_page(self, response):
        next_page = response.meta.get('page') + 1
        json_data = json.loads(response.text)
        if json_data.get('type') != 'success':
            return
        articles = scrapy.Selector(text=json_data.get('html')).css('article')
        for article in articles:
            yield {
                'author': article.css('div.author-meta a ::text').extract_first(),
                'date': article.css('div.clock-meta a ::text').extract_first(),
                'title': article.css('h1.entry-title ::text').extract_first()
            }
        yield scrapy.FormRequest(
            self.scrolling_url, formdata={'action': 'infinite_scroll', 'page': str(next_page), 'order': 'DESC'},
            callback=self.parse_page, meta={'page': next_page}
        )
