# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarreportsItem(scrapy.Item):
    # define the fields for your item here like:
    # 汽车名字
    name = scrapy.Field()
    # 销售数量
    count = scrapy.Field()
    # 销售价格
    price = scrapy.Field()

    # pass
