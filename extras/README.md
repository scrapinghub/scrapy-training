Extra
=====
Item Loaders provide a convenient way to structure your code, resulting in tidier spiders.

## Topics
* Generating Items
* Item Loaders


## Example
1. A regular spider generating schema-less JSON items: [`spider_1_no_item.py`](itemloaders_example/itemloaders_example/spiders/spider_1_no_item.py)
2. Same spider as above, but generating [`Item`](https://doc.scrapy.org/en/latest/topics/items.html) objects instead of dictionaries: [`spider_2_with_item.py`](itemloaders_example/itemloaders_example/spiders/spider_2_with_item.py)
3. Same spider, but using an [`Item Loader`](https://doc.scrapy.org/en/latest/topics/loaders.html) to populate the item object: [`spider_3_with_itemloader.py`](itemloaders_example/itemloaders_example/spiders/spider_3_with_itemloader.py) and [`items.py`](itemloaders_example/itemloaders_example/items.py)
4. Same spider, but using a custom Item Loader: [`spider_4_custom_itemloader.py`](itemloaders_example/itemloaders_example/spiders/spider_4_custom_itemloader.py) and [`itemloaders.py`](itemloaders_example/itemloaders_example/itemloaders.py)
5. Spider for books.toscrape.com using Item Loaders and input/output processors to format the data: [`spider_5_books_with_itemloader.py`](itemloaders_example/itemloaders_example/spiders/spider_5_books_with_itemloader.py) and [`items.py`](itemloaders_example/itemloaders_example/items.py)


## References
* [Items reference](https://doc.scrapy.org/en/latest/topics/items.html)
* [Item Loaders reference](https://doc.scrapy.org/en/latest/topics/loaders.html)
