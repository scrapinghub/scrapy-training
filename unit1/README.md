Unit 1: Scraping the Web with Scrapy
====================================

This unit covers the basics of web scraping with a special focus on data extraction with Scrapy.

**[Click here to view this unit's slides](https://docs.google.com/presentation/d/1IYFmTeAyOSwMUtQkrjWuAkfcqOMWNlY6wmn1DgA5ZB4/edit)**


## Sample Spiders
1. Spider that saves 2 pages from quotes.toscrape.com to the disk: [`spider_1_quote.py`](spiders/spider_1_quotes.py), [`spider_2_quotes.py`](spiders/spider_2_quotes.py)
2. Spider that scrapes quotes.toscrapes.com: [`spider_3_quotes.py`](spiders/spider_3_quotes.py)


## Hands-on

#### 1. Reddit spider
Build a spider to extract `title`, `link`, `username`, `user_url`, `score` and `time` from each submission in the front page of reddit's [/r/programming](http://reddit.com/r/programming) and [/r/python](http://reddit.com/r/python).

[Check out the spider **once you're done**.](spiders/spider_4_reddit.py)

#### 2. Books spider
Build a spider for [books.toscrape.com](http://books.toscrape.com) that extracts `title`, `rating`, `price`, `stock` and `category` from the URLs listed in [this file](spiders/urls.txt) (it can be stored locally alongside your spider).

[Check out the spider **once you're done**.](spiders/spider_5_books.py)

## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Parsel (the extraction library behind Scrapy) documentation](https://parsel.readthedocs.io/en/latest/usage.html#getting-started)
* [The 30 CSS selectors you must memorize](https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048)
