import json


class SaveToFilesPipeline(object):

    def open_spider(self, spider):
        self.fps = {}

    def process_item(self, item, spider):
        author_name = item.get('author', '')
        filename = '{}.jl'.format('_'.join(author_name.lower().split()))
        if filename not in self.fps:
            self.fps[filename] = open(filename, 'w')
        self.fps[filename].write(json.dumps(item) + '\n')
        return item

    def close_spider(self, spider):
        for fp in self.fps.values():
            fp.close()
