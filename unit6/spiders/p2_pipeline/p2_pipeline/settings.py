BOT_NAME = 'p2_pipeline'

SPIDER_MODULES = ['p2_pipeline.spiders']
NEWSPIDER_MODULE = 'p2_pipeline.spiders'

ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    'p2_pipeline.pipelines.MongoDbPipeline': 300,
}

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'items'
