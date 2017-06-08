# -*- coding:utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst


def strip_quotes(value):
    return value.replace('“', '').replace('”', '')


class QuoteLoader(ItemLoader):
    default_output_processor = TakeFirst()
    text_in = MapCompose(strip_quotes)
    tags_out = Join(',')
