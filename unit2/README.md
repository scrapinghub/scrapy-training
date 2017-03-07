Unit 2: Navigating websites with Scrapy
=======================================

This unit build upon the previous one and covers how to crawl websites with Scrapy. Crawling a website means basically following the links found in the pages, so that the spider visits all the pages it needs.


## Sample Spiders
1. Spider that follows pagination links to scrape [quotes.toscrape.com](http://quotes.toscrape.com): [[spider_1_quotes_pagination.py](spiders/spider_1_quotes_pagination.py)]
2. Spider that extracts authors' data from details pages in [quotes.toscrape.com](http://quotes.toscrape.com): [[spider_2_authors_details.py](spiders/spider_2_authors_details.py)]
3. Spider that extracts the quotes alongside authors's information from [quotes.toscrape.com](http://quotes.toscrape.com): [[spider_3_quotes_authors.py](spiders/spider_3_quotes_authors.py)]
4. Spider that extracts books' data from [goodreads.com](http://goodreads.com): [[spider_4_goodreads_link_finder.py](spiders/spider_4_goodreads_link_finder.py)]
5. CrawlSpider that extracts books' data from [goodreads.com](http://goodreads.com): [[spider_5_crawlspider.py](spiders/spider_5_crawlspider.py)]
6. SiteMap example: [[spider_6_sitemap_blog.py](spiders/spider_6_sitemap_blog.py)]



## Hands-on

#### 1. Books Crawler (without CrawlSpider)
**Without using CrawlSpider**, build a spider to extract `title`, `rating` (int), `price` (float), `stock` and  `cover URL` from all the 1000 books available in [books.toscrape.com](http://books.toscrape.com).

[Check out the spider **once you're done**.](spiders/spider_7_books.py)

#### 2. Books Crawler (with CrawlSpider)
Build a spider with the same requirements as the previous exercise, but now using `CrawlSpider`.

[Check out the spider **once you're done**.](spiders/spider_8_books_crawlspider.py)

## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [CrawlSpider documentation](https://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider)
* [SitemapSpider documentation](https://doc.scrapy.org/en/latest/topics/spiders.html#sitemapspider)
* [SitemapSpider blog post](https://blog.scrapinghub.com/2016/02/24/scrapy-tips-from-the-pros-february-2016-edition/)
