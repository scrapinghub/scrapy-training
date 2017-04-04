Unit 6: Extending Scrapy
========================

This unit covers how to extend Scrapy capabilities, either via Item Pipelines or Middlewares.

**[Check out the slides of this unit](https://docs.google.com/presentation/d/1cPGni3rAhE-vQoDdxOJSuXrqioHDvBQOpufDQNyYQOM/pub?start=false&loop=false&delayms=300000000)**


## Sample Spiders
1. A project including a Pipeline that drops items that don't have `tags`: [`p1_pipeline`](spiders/p1_pipeline)
2. A project including a Pipeline that stores scraped data in MongoDB: [`p2_pipeline`](spiders/p2_pipeline)
3. A project with 2 spider middlewares: [`p3_spider_middleware`](spiders/p3_spider_middleware)


## Hands-on

#### 1. Pipeline
Build an item pipeline that stores the quotes from each author from http://quotes.toscrape.com in a separate json-lines file.

* Albert Einstein → albert_einstein.jl
* Jane Austen → jane_austen.jl
* etc

[Check out the project **once you're done**.](spiders/p4_pipeline_handson)


#### 2. Downloader Middleware
Build a downloader middleware to fetch and render pages using Selenium + PhantomJS instead of the Scrapy downloader.

* Make sure users can disable it either via settings or in a per-request basis.


[Check out the project **once you're done**.](spiders/p5_downloader_middleware_handson)


## References
* [Scrapy Architecture](https://doc.scrapy.org/en/latest/topics/architecture.html)
* [Item pipelines](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)
* [Spider middlewares](https://doc.scrapy.org/en/latest/topics/spider-middleware.html)
* [Downloader middlewares](https://doc.scrapy.org/en/latest/topics/downloader-middleware.html)
* [Scrapy Signals](https://doc.scrapy.org/en/latest/topics/signals.html)
