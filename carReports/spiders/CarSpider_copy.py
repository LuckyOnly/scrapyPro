# coding:utf-8

import scrapy


# 实例化浏览器可以通过process_response中的spider获取
# 实例化浏览器可以写在这里
class CarSpider(scrapy.Spider):
    # name定义spider名字的字符串(string)
    name = "car2"

    # 这是一个可选的属性，包含了爬虫允许爬取的域名列表。当 OffsiteMiddleware 设置启用时，域名不在列表中的 URL 不会被跟进。
    # allowed_domain = ['dongchedi.com']

    # URL列表。
    start_urls = ['https://www.dongchedi.com/sales']

    def parse(self, response, **kwargs):
        self.log('Hi,this is a item page! %s ' % response.url)
        # 获取href
        # hrefs = response.xpath('.//div[@id="__next"]/main/div/div/div/a/@href')
        hrefs = response.xpath('.//div[@id="__next"]/div[1]/div[2]/div/div[1]/div[2]/a/@href')
        print('1234', hrefs)
        # 遍历指定的链接
        for href in hrefs:
            print(href.extract())
            full_url = 'https://www.dongchedi.com' + str(href.extract())

            # 每次爬取下一个页面，然后保存获取的值
            yield scrapy.Request(full_url, callback=self.parse_question)


    def parse_question(self, response):

        filename = 'sales.txt'
        # import os
        # if os.path.exists(filename):
        #     os.remove(filename)
        with open(filename, 'a') as f:
            name = response.xpath(
                './/div[@id="__next"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/h1/text()').extract()
            print(name)
            price = response.xpath(
                './/div[@id="__next"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/p[2]/text()').extract()

            print(price)

            try:
                if len(name) > 0:
                    f.write(name[0])
                    f.write(",")
                if len(price) > 0:
                    f.write(price[0])
                    f.write('\n')


            except ValueError:
                f.close()
        #
