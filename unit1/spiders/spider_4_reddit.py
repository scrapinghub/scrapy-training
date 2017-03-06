import scrapy
from datetime import datetime


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
                # when score is 0, reddit show a bullet point instead of a 0
                'score': int(thing.css('.score.unvoted::text').re_first('(\d+)') or 0),
                'time': datetime.strptime(
                    thing.css('time::attr(datetime)').extract_first(),
                    '%Y-%m-%dT%H:%M:%S+00:00'
                ),
            }
