Unit 4: Handling HTML Forms
===========================

This unit covers how to post data to web servers, so that our spiders can perform searches and authenticate themselves in websites that require that.

**[Click here to view this unit's slides](https://docs.google.com/presentation/d/1T67JklviVFD-HkP21GxSIgr_BQY6lBbJY83eZTnkFnU/edit)**


## Sample Spiders
1. A simple spider to demonstrate how `FormRequest` works: [`spider_1_basic_form.py`](spiders/spider_1_basic_form.py)
2. A spider that authenticates into quotes.toscrape.com: [`spider_2_login.py`](spiders/spider_2_login.py)
3. Same as #2, but using `FormRequest.from_response()` method: [`spider_3_login.py`](spiders/spider_3_login.py)

## Hands-on

#### 1. Hacker News spider
Build a Spider that authenticates into news.ycombinator.com and then extracts your own username and amount of points from the news page top (fake user/pass: `scrape1123`/`scrape1123`).

[Check out the spider **once you're done**.](spiders/spider_4_handson_1.py)

#### 2. Quotes filtering crawler
Build a spider that scrapes all the quotes from every author listed in [quotes.toscrape.com/search.aspx](http://quotes.toscrape.com/search.aspx).

[Check out the spider **once you're done**.](spiders/spider_5_handson_2.py)

## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Scrapy docs on FormRequest](https://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects)
* [Scraping websites based on ViewStates with Scrapy](https://blog.scrapinghub.com/2016/04/20/scrapy-tips-from-the-pros-april-2016-edition/)
