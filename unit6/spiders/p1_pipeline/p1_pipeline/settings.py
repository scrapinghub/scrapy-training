# -*- coding: utf-8 -*-

BOT_NAME = 'p1_pipeline'

SPIDER_MODULES = ['p1_pipeline.spiders']
NEWSPIDER_MODULE = 'p1_pipeline.spiders'

ROBOTSTXT_OBEY = True


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'p1_pipeline.pipelines.DropNoTagsPipeline': 300,
}
