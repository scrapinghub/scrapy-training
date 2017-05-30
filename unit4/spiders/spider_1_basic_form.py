import scrapy


class BasicFormSpider(scrapy.Spider):
    name = 'basic-form'

    def start_requests(self):
        formdata = {
            'custname': 'Valdir',
            'custtel': '99333322',
            'custemail': 'valdir@scrapinghub.com',
            'size': 'large',
            'topping': ['bacon', 'cheese'],
            'delivery': '21:00',
            'comments': 'My dog is hungry!'
        }
        yield scrapy.FormRequest(
            'http://httpbin.org/post',
            formdata=formdata,
            callback=self.parse_form_results
        )

    def parse_form_results(self, response):
        # this website just returns a JSON response with the same
        # contents as the ones passed in the form.
        self.log(response.body)
