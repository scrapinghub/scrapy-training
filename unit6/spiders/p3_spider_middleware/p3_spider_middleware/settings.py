BOT_NAME = 'p3_spider_middleware'

SPIDER_MODULES = ['p3_spider_middleware.spiders']
NEWSPIDER_MODULE = 'p3_spider_middleware.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
    'p3_spider_middleware.middlewares.IgnoreEmptyResponseMiddleware': 540,
    'p3_spider_middleware.middlewares.AddUrlFieldMiddleware': 543,
}
