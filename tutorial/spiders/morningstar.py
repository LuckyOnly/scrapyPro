# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# import scrapy
# from tutorial.items import DmozItem
#
#
# class DmozSpider(Spider):
#     name = "morningstar"
#     allowed_domains = ["cn.morningstar.com"]
#     start_urls = [
#         "http://cn.morningstar.com/fundselect/default.aspx?star=5",
#     ]
#
#     def parse(self, response):
#         for href in response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]/a/@href').extract():
#             url = response.urljoin(href)#"http://cn.morningstar.com",
#             yield scrapy.Request(url, callback=self.parse_dir_contents)
#
#     def parse_dir_contents(self, response):
#         """
#         The lines below is a spider contract. For more info see:
#         http://doc.scrapy.org/en/latest/topics/contracts.html
#
#         @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
#         @scrapes name
#         """
#         sites=response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]')
#         # sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
#         items = []
#
#         for site in sites:
#             item = DmozItem()
#             item['title'] = site.xpath(
#                 'a/text()').extract()
#             print item['name']
#             item['link'] = site.xpath(
#                 'a/@href').extract()
#             item['desc'] = site.css(
#                 'a/@target').extract()
#             items.append(item)
#
#         return items
#coding:utf-8
#-*-coding:utf-8-*-
from scrapy.spiders import Spider
import scrapy
import os

class StackOverflowSpider(Spider):
    name = 'morningstar'
    start_urls = ['http://cn.morningstar.com/fundselect/default.aspx?star=5']

    def parse(self, response):
        for href in response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

# 123
    def parse_question(self, response):
        yield {
            'title': response.xpath('//div[@id="qt_fund"]/span[@class="name"]/text()').extract(),
            'link': response.url,
            # 'attri': response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]/a/@target').extract(),

        }
'''
    def closed(self, reason):
        from scrapy.mail import MailSender

        mailer = MailSender(
            smtphost="smtp.163.com",
            mailfrom="zongff9095@163.com",
            smtpuser="zongff9095@163.com",
            smtppass="zff90111",
            smtpport=25
        )
        f = open(os.getcwd() + r"\List.json")
        line = f.readline().decode('unicode_escape')
        textr = []
        while line:
            textr.append(line)
            line = f.readline().decode('unicode_escape')
        body = ' '.join(textr)

        subject = u'scrapy emails'
'''
        # mailer.send(to=["1047670763@qq.com", "1047670763@qq.com"], subject=subject.encode("utf-8"), body=body.encode("utf-8"))
