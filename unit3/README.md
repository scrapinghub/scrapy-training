Unit 3: Running Spiders in the Cloud
=======================================

This unit describes how to deploy scrapy spiders to [Scrapy Cloud](http://app.scrapinghub.com) and how to leverage from this platform.

**[Click here to view this unit's slides](https://docs.google.com/presentation/d/1nEUGJ-slHYNemYvo8WEBizDtYDCikWcnNXfhUhHFDRw/edit)**


## Sample Spiders
1. A simple project to demonstrate deploy: [[p1_first_deploy](spiders/p1_first_deploy/)]
2. A project to deploy with dependencies: [[p2_dependencies](spiders/p2_dependencies/)]
3. A project to deploy with Python Scripts: [[p3_scripts](spiders/p3_scripts/)]



## Hands-on

#### 1. Reddit Crawler
Create a crawler to fetch the 100 hottest submissions from reddit.com/r/programming (to run on Scrapy Cloud).


#### 2. Ranking submissions
Create a CLI app to fetch the scraped data from Scrapy Cloud and list the top 10 submissions from the latest crawl, based on the score below:

    new_score = S * C * K

        S → current score on reddit
        C → number of comments
        K → original poster's comments karma

[Check out the project **once you're done**.](spiders/p4_handson/)


## References
* [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [Dependencies in Scrapy Cloud Projects](http://help.scrapinghub.com/scrapy-cloud/dependencies-in-scrapy-cloud-projects)
* [Running custom Python scripts in Scrapy Cloud](http://help.scrapinghub.com/scrapy-cloud/running-custom-python-scripts)
* [Blog post: How to run Python in Scrapy Cloud](https://blog.scrapinghub.com/2016/09/28/how-to-run-python-scripts-in-scrapy-cloud/)
