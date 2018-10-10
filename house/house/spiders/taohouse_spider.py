# -*-coding:utf-8-*-
__author__ = 'JamesDing'
# *******************************************************************
#     Filename @  taohouse_spider.py
#       Author @  James
#  Create date @  2018/10/10 0010 21:22
#        Email @  zongff9095@163.com
#  Description @  邮件发送
#      license @ (C) Copyright 2011-2018, DevOps Corporation Limited.
# ********************************************************************

from scrapy.spiders import Spider
import scrapy

class HoseSpider(Spider):
    name = 'def'
    start_urls = ['http://newhouse.nj.house365.com/house/dist-10/']

    def parse(self, response):
        for href in response.xpath('//div/div/div/div/div/div/h3/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)


    def parse_question(self, response):
        price_name_1 = response.xpath('//div[@class="h22 over_hide f14"]/div/text()').extract()
        for name in price_name_1:
            if name == u'最新报价：':
                yield {
                'title': response.xpath('//div/div/div/div/h1/text()').extract(),
                'link': response.url,
                'price': response.xpath('//div/div/div/div/div/div/span/text()')[0].extract()
                # 'price': response.xpath('//div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/span/text()')[0].extract()

                }
                break
            else:
                yield {
                'title': response.xpath('//div/div/div/div/h1/text()').extract(),
                'link': response.url,
                'price': response.xpath('//div/div/div/span/em/text()')[0].extract()
                }
                break