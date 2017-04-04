Unit 3: Running Spiders in the Cloud
=======================================

This unit describes how to deploy scrapy spiders to [Scrapy Cloud](http://app.scrapinghub.com) and how to leverage from this platform.

**[Check out the slides for this unit](https://docs.google.com/presentation/d/1nEUGJ-slHYNemYvo8WEBizDtYDCikWcnNXfhUhHFDRw/pub?start=false&loop=false&delayms=300000000)**


## Sample Spiders
1. A simple project to demonstrate deploy: [`p1_first_deploy`](spiders/p1_first_deploy/)
2. A project to deploy with dependencies: [`p2_dependencies`](spiders/p2_dependencies/)
3. A project to deploy with Python Scripts: [`p3_scripts`](spiders/p3_scripts/)


## Hands-on

#### 1. Deploy the books crawler
Deploy the crawler for books.toscrape.com built in [unit 2](../unit2) to Scrapy Cloud.

a. Run the spider without touching any settings
b. Run the spider, but now with `DOWNLOAD_DELAY = 1` set via web UI

[Check out the project **once you're done**.](spiders/p4_bookscrawler/)


#### 2. Reddit Ranker
Create a crawler to fetch the 100 hottest submissions from reddit.com/r/programming (to run on Scrapy Cloud).

After that, create a CLI app to fetch the scraped data from Scrapy Cloud and list the top 10 submissions from the latest crawl, based on the score below:

    new_score = S * C * K

        S → current score on reddit
        C → number of comments
        K → original poster's comments karma

[Check out the project **once you're done**.](spiders/p5_handson/)


## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Dependencies in Scrapy Cloud Projects](http://help.scrapinghub.com/scrapy-cloud/dependencies-in-scrapy-cloud-projects)
* [Running custom Python scripts in Scrapy Cloud](http://help.scrapinghub.com/scrapy-cloud/running-custom-python-scripts)
* [Blog post: How to run Python in Scrapy Cloud](https://blog.scrapinghub.com/2016/09/28/how-to-run-python-scripts-in-scrapy-cloud/)
