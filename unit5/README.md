Unit 5: Scraping JavaScript based pages
=======================================

In this unit, we will see how to extract data from JS based pages.

**[Check out the slides for this unit](https://docs.google.com/presentation/d/1HAMMWLDQ7wbxZVBSiKrsiWVXyt2ok8YcKHRrdQMRVM8/pub?start=false&loop=false&delayms=300000000)**


## Sample Spiders
1. A spider using [js2xml](http://github.com/scrapinghub/js2xml) to extract alternate color from products: [`spider_1_hm_js2xml.py`](spiders/spider_1_hm_js2xml.py)

2. A crawler rendering a JS based page via [Splash](http://github.com/scrapinghub/splash): [`p2_quotes_splash/`](spiders/p2_quotes_splash/)

3. Same as the previous one, but now using [Selenium](http://www.seleniumhq.org) and [PhantomJS](http://phantomjs.org/): [`spider_3_quotes_selenium.py`](spiders/spider_3_quotes_selenium.py)

4. A spider built with Selenium + Python (not using Scrapy): [`spider_4_standalone_selenium.py`](spiders/spider_4_standalone_selenium.py)

5. A spider that scrapes data using AJAX calls to simulate infinite scrolling: [`spider_5_ajax_pythonhelp.py`](spiders/spider_5_ajax_pythonhelp.py)



## Hands-on

#### 1. Infinite Scrolling (AJAX)
Build a spider to fetch all quotes from http://quotes.toscrape.com/scroll.

[Check out the project **once you're done**.](spiders/spider_6_ajax_quotes.py)


#### 2. JavaScript
Build a spider to fetch all quotes from http://quotes.toscrape.com/js using [js2xml](http://github.com/scrapinghub/js2xml).

[Check out the project **once you're done**.](spiders/spider_7_quotes_js2xml.py)


## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [How to deploy a PhantomJS spider to Scrapy Cloud](https://blog.scrapinghub.com/2016/09/08/how-to-deploy-custom-docker-images-for-your-web-crawlers/)
* [js2xml project page](http://github.com/scrapinghub/js2xml)
* [PhantomJS project page](http://phantomjs.org)
* [Splash project page](http://github.com/scrapinghub/splash)
* [SeleniumHQ project page](http://www.seleniumhq.org)
