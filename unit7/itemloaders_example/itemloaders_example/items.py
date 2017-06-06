# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst


def strip_quotes(value):
    return value.replace('“', '').replace('”', '')


class Quote(scrapy.Item):
    text = scrapy.Field(
        input_processor=MapCompose(strip_quotes),
        output_processor=TakeFirst(),
    )
    author_name = scrapy.Field(
        output_processor=TakeFirst(),
    )
    # generates tags as CSV
    tags = scrapy.Field(
        output_processor=Join(','),
    )
    ts = scrapy.Field()
