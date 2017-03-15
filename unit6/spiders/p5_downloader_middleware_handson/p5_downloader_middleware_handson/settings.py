BOT_NAME = 'p5_downloader_middleware_handson'

SPIDER_MODULES = ['p5_downloader_middleware_handson.spiders']
NEWSPIDER_MODULE = 'p5_downloader_middleware_handson.spiders'

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    'p5_downloader_middleware_handson.middlewares.SeleniumDownloaderMiddleware': 543,
}
SELENIUM_ENABLED = True
