# -*- coding: utf-8 -*-
import scrapy


class RedditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ['http://reddit.com/r/programming']
    depth_level = 0

    def parse(self, response):
        self.depth_level += 1
        for thing in response.css('.thing:not(.stickied)'):
            item = {
                'title': thing.css('.title::text').extract_first(),
                'link': thing.css('.title > a::attr(href)').extract_first(),
                'score': int(thing.css('.score.unvoted::text').re_first('(\d+)') or 0),
                'number_of_comments': int(thing.css('a.comments ::text').re_first('\d+') or 0),
            }
            user_url = thing.css('a.author::attr(href)').extract_first()
            yield scrapy.Request(
                user_url,
                meta={'item': item},
                dont_filter=True,
                callback=self.parse_user
            )

        next_page_url = response.css('span.next-button a::attr(href)').extract_first()
        if self.depth_level < 4 and next_page_url:
                yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_user(self, response):
        item = response.meta.get('item')
        item['user_karma'] = response.css('span.comment-karma::text').extract_first()
        item['user_karma'] = float(item['user_karma'].replace(',', ''))
        yield item
