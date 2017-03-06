import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    start_urls = [
        'http://reddit.com/r/programming',
        'http://reddit.com/r/python',
    ]

    def parse(self, response):
        # ':not(.stickied)' avoids scraping announcements that arte sticked to the top
        for thing in response.css('.thing:not(.stickied)'):
            yield {
                'title': thing.css('.title::text').extract_first(),
                'link': thing.css('.title > a::attr(href)').extract_first(),
                'user_name': thing.css('a.author::text').extract_first(),
                'user_url': thing.css('a.author::attr(href)').extract_first(),
                'score': thing.css('.score.unvoted::text').extract_first(),
                'time': thing.css('time::attr(datetime)').extract_first(),
            }
