import scrapy
import js2xml


class HMJs2XmlSpider(scrapy.Spider):
    name = 'hm-js2xml'
    start_urls = [
        'http://www2.hm.com/en_gb/productpage.0437668004.html',
    ]

    def parse(self, response):
        js_code = response.xpath('//script[contains(., "productArticleDetails")]/text()').extract_first()
        parsed_js = js2xml.parse(js_code)
        sel = scrapy.Selector(root=parsed_js)
        for product in sel.css('property[name="categoryParentKey"] ~ property'):
            yield {
                'descr': product.css('property[name="description"] > string::text').extract_first(),
                'price': product.css('property[name="priceValue"] > string::text').extract_first(),
                'color': product.css('property[name="name"] > string::text').extract_first(),
                'url': response.urljoin(product.css('property[name="url"] > string::text').extract_first()),
            }
