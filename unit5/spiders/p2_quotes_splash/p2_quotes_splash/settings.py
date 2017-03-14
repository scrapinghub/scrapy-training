# -*- coding: utf-8 -*-

BOT_NAME = 'p2_quotes_splash'
SPIDER_MODULES = ['p2_quotes_splash.spiders']
NEWSPIDER_MODULE = 'p2_quotes_splash.spiders'
ROBOTSTXT_OBEY = True


# Splash settings
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
# Splash running on a local Docker container
SPLASH_URL = 'http://192.168.99.100:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
