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
from scrapy.spiders import Spider
import scrapy


class StackOverflowSpider(Spider):
    name = 'morningstar'
    start_urls = ['http://cn.morningstar.com/fundselect/default.aspx?star=5']

    def parse(self, response):
        for href in response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {#html/body/form/div[6]/div/div[2]/ul[3]/li[2]/span
            'title': response.xpath('//div[@id="qt_fund"]/span[@class="name"]').extract(),
            'link': response.xpath('//div[@id="qt_manager"]/ul[1]/li[1]/a').extract(),
            # 'attri': response.xpath('//table[@id="ctl00_cphMain_gridResult"]/tr/td[3]/a/@target').extract(),

        }