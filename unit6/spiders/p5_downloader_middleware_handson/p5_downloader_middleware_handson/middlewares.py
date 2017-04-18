from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import NotConfigured
from selenium import webdriver


class SeleniumDownloaderMiddleware(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    @classmethod
    def from_crawler(cls, crawler):
        m = cls()
        if not crawler.settings.getbool('SELENIUM_ENABLED'):
            raise NotConfigured()
        crawler.signals.connect(m.spider_closed, signal=signals.spider_closed)
        return m

    def process_request(self, request, spider):
        if request.meta.get('nojs'):
            # disable js rendering in a per-request basis
            return
        self.driver.get(request.url)
        content = self.driver.page_source
        return HtmlResponse(request.url, body=content, encoding='utf-8')

    def spider_closed(self, spider):
        self.driver.close()
