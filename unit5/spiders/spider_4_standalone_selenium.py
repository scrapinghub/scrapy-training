import parsel
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def scrape():
    driver = webdriver.PhantomJS()
    driver.get('http://quotes.toscrape.com/js-onclick')
    while True:
        sel = parsel.Selector(text=driver.page_source)
        for quote in sel.css('div.quote'):
            print({
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            })
        try:
            next_button = driver.find_element_by_css_selector('li.next > a')
            next_button.click()
        except NoSuchElementException:
            break


if __name__ == '__main__':
    scrape()
