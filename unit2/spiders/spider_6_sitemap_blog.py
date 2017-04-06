from scrapy.spiders import SitemapSpider


class BlogSitemapSpider(SitemapSpider):
    name = 'blog-spider'
    sitemap_urls = ['http://pythonhelp.wordpress.com/sitemap.xml']
    sitemap_rules = [
        ('.com/\d{4}/', 'parse_blogpost'),
        ('', 'parse')
    ]
    download_delay = 1.5

    def parse(self, response):
        self.log("default parsing method for {}".format(response.url))

    def parse_blogpost(self, response):
        self.log("parse_blogpost method for {}".format(response.url))
