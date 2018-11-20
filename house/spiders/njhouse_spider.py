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

global count
count = 2

class HoseSpider(Spider):
    # print '爬取数据'
    name = 'nj'
    start_urls = ['http://www.njhouse.com.cn/2016/spf/list.php?dist=%BD%AD%C4%FE&use=1&saledate=5&pgno=1','http://www.njhouse.com.cn/2016/spf/list.php?dist=%D3%EA%BB%A8%CC%A8&use=1&saledate=5&pgno=1']
    def parse(self, response):
        # 选择所有的链接
        global count
        for href in response.xpath('.//*[@id="news_se_frm"]/div/table/tbody/tr[1]/td[3]/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)
        #下一页
        next_page = response.xpath('//a[@class="bt_next"]/text()').extract()
        next_url = response.xpath('//div[@class="navs_block clearfix"]/a/@href').extract()
        if next_page[0] ==u"下一页" and count<len(next_url)-1:
            url = "http://www.njhouse.com.cn/2016/spf/list.php?dist=%BD%AD%C4%FE&use=1&saledate=5&pgno="+str(count)
            yield scrapy.Request(url,callback=self.parse)
            count = count + 1


    def parse_question(self, response):
        name = response.xpath('//div[@class="main"]/div[@class="business_centers"]/div/div[@class="spf_del_title clearfix"]/h2/text()').extract()
        yield {
            "name":name,
            'cdate': response.xpath('//table[@class="spf_table"]/tbody/tr[5]/td[2]/text()').extract(),
            'price': response.xpath('//div[@class="spf_block_list spf_block_first"]/table[1]/tbody/tr[2]/td[6]/text()').extract(),
            'unsale': response.xpath('//div[@class="spf_block_list spf_block_first"]/table[1]/tbody/tr[3]/td[2]/text()').extract(),
            'address':response.xpath('//table[@class="spf_table"]/tbody/tr[1]/td[2]/text()').extract(),
            'manager':response.xpath('//table[@class="xmgk"]/tbody/tr[1]/td[2]/text()').extract(),
            'engineer':response.xpath('//table[@class="spf_table"]/tbody/tr[3]/td[2]/a/text()').extract(),
            'link':response.url
        }



