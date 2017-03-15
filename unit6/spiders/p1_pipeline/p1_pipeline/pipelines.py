from scrapy.exceptions import DropItem


class DropNoTagsPipeline(object):
    def process_item(self, item, spider):
        if not item.get('tags', []):
            raise DropItem('item doesnt contain tags')
        return item
