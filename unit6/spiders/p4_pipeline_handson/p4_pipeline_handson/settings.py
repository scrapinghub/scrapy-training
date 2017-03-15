BOT_NAME = 'p4_pipeline_handson'

SPIDER_MODULES = ['p4_pipeline_handson.spiders']
NEWSPIDER_MODULE = 'p4_pipeline_handson.spiders'

ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    'p4_pipeline_handson.pipelines.SaveToFilesPipeline': 300,
}
