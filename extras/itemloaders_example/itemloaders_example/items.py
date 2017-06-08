# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst


def strip_quotes(value):
    return value.replace('“', '').replace('”', '')


class QuoteItem(scrapy.Item):
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
    url = scrapy.Field(
        output_processor=TakeFirst(),
    )


def get_stock_from_str(s):
    m = re.search(r'(\d+)', s)
    if m:
        return m.group(1).strip()


def get_numerical_rating_from_classname(classname):
    rating_str = classname.split(' ')[-1]
    ratings_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }
    return ratings_map.get(rating_str.lower(), '')


class BookItem(scrapy.Item):
    rating = scrapy.Field()
    title = scrapy.Field(
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(lambda s: s[1:], float),
        output_processor=TakeFirst(),
    )
    stock = scrapy.Field(
        input_processor=MapCompose(get_stock_from_str, int),
        output_processor=TakeFirst(),
    )
    category = scrapy.Field(
        input_processor=MapCompose(lambda s: s.strip()),
        output_processor=TakeFirst(),
    )
    rating = scrapy.Field(
        input_processor=MapCompose(get_numerical_rating_from_classname),
        output_processor=TakeFirst()
    )
