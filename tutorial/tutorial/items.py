# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #首先根据需要从dmoz.org获取到的数据对item进行建模。 我们需要从dmoz中获取名字，url，以及网站的描述。
    title=scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()
