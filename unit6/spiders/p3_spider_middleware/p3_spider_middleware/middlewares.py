import logging

logger = logging.getLogger(__name__)


class EmptyResponseException(Exception):
    pass


class AddUrlFieldMiddleware(object):
    """Adds to the item a field containing the response URL from
       where the item has been generated.
    """

    def process_spider_output(self, response, result, spider):
        for r in result:
            if isinstance(r, dict):
                if 'url' not in r:
                    r['url'] = response.url
            yield r


class IgnoreEmptyResponseMiddleware(object):
    """Ignores responses with empty bodies."""

    def process_spider_input(self, response, spider):
        if not response.text:
            raise EmptyResponseException()
        else:
            return None

    def process_spider_exception(self, response, exception, spider):
        if isinstance(exception, EmptyResponseException):
            logger.info('Response from {} ignored due to empty body.'.format(response.url))
            spider.crawler.stats.inc_value('emptyresponse/response_ignored_count')
            return []
