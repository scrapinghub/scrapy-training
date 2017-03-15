from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from scrapy.exceptions import DropItem


class MongoDbPipeline(object):
    collection_name = 'quotes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        try:
            self.db[self.collection_name].insert(dict(item))
            return item
        except DuplicateKeyError:
            raise DropItem('Duplicated item')

    def close_spider(self, spider):
        self.client.close()
