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
    # start_urls = ['http://newhouse.nj.house365.com/house/dist-10/']
    start_urls = ['http://newhouse.nj.house365.com/house/dist-11/']

    def parse(self, response):
        for href in response.xpath('//div/div/div/div/div/div/h3/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)
        #下一页
        next_page = response.xpath('//div/div/div[@class="sm_page mt20 pageList"]/a/text()').extract()
        next_url = response.xpath('//div/div/div[@class="sm_page mt20 pageList"]/a/@href').extract()
        i=0
        while i < len(next_page):
            if next_page[i] ==u"下一页":
                yield scrapy.Request(next_url[i],callback=self.parse)
            i+=1


    def parse_question(self, response):
        price_name_1 = response.xpath('//div[@class="h22 over_hide f14"]/div/text()').extract()
        if price_name_1:
            for name in price_name_1:
                if name == u'最新报价：':
                    yield {
                    'title': response.xpath('//div/div/div/div/h1/text()').extract(),
                    'link': response.url,
                    'price': response.xpath('//div/div/div/div/div/div/span/text()')[0].extract(),
                    'status':response.xpath('//div/div[1]/div[2]/div[1]/span[@class="org_4"]/text()')[0].extract(),
                    'type':response.xpath(u'normalize-space(//div/div/div/div/div[contains(text(),"项目类型")]/text())')[0].extract()
                    }
                    break
        else:
            yield {
            'title': response.xpath('//div/div/div/div/h1/text()').extract(),
            'link': response.url,
            'price': response.xpath('//div/div/div/span/em/text()')[0].extract(),
            'status': response.xpath('//div/div[1]/div[2]/div[1]/span[@class="org_4"]/text()')[0].extract(),
            'type': response.xpath('normalize-space(//div/div/div/div/span[@class="pr20 w200 fl nowrap"]/text())')[0].extract()
            }


