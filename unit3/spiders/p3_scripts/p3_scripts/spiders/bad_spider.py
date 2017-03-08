# -*- coding: utf-8 -*-
import scrapy


class SpiderWithErrors(scrapy.Spider):
    name = "bad"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        raise ValueError('Oops, this spider has errors')
