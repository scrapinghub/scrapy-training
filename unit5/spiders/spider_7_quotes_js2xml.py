import scrapy
import js2xml


class QuotesJs2XmlSpider(scrapy.Spider):
    name = 'quotes-js2xml'
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        # extract the JS code block from the HTML page
        script = response.xpath('//script[contains(., "var data =")]/text()').extract_first()
        # build an XML tree from the JS code
        js_as_xml_tree = js2xml.parse(script)
        # select only the array object containing the quotes in the XML tree
        js_data_array = js_as_xml_tree.xpath('//var[@name="data"]')[0][0]
        # iterate over a list of dictionaries from the JS array
        for quote in js2xml.jsonlike.make_dict(js_data_array):
            yield quote

        link_next = response.css('li.next a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))

    def alternative_parse_method(self, response):
        # An alternative would be to build a Scrapy selector from the JS string
        # and extract the data using CSS selectors
        script = response.xpath('//script[contains(., "var data =")]/text()').extract_first()
        sel = scrapy.Selector(root=js2xml.parse(script))
        for quote in sel.css('var[name="data"] > array > object'):
            yield {
                'text': quote.css('property[name="text"] > string::text').extract_first(),
                'author': quote.css('property[name="author"] property[name="name"] > string::text').extract_first(),
                'tags': quote.css('property[name="tags"] string::text').extract(),
            }

        link_next = response.css('li.next a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))
