# -*-coding:utf-8-*-
__author__ = 'JamesDing'
# *******************************************************************
#     Filename @  house_spider.py
#       Author @  James
#  Create date @  2018/10/9 0009 21:06
#        Email @  zongff9095@163.com
#  Description @  邮件发送
#      license @ (C) Copyright 2011-2018, DevOps Corporation Limited.
# ********************************************************************
from scrapy.spiders import Spider
import scrapy

class HoseSpider(Spider):
    name = 'abc'
    start_urls = ['http://nanjing.newhouse.fang.com/house/s/yuhua/a77/']

    def parse(self, response):
        for href in response.xpath('.//*[@id="newhouse_loupai_list"]/ul/li/div/div/div/div/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)


    def parse_question(self, response):
        yield {
            'title': response.xpath('//div[@class="main_1200 tf"]/div[3]/div[2]/div[1]/div[1]/div/h1/strong/text()').extract(),
            'link': response.url,
            'price': response.xpath('//div[@class="lp-info"]/div[@class="l-price"]/span/text()').extract()

        }