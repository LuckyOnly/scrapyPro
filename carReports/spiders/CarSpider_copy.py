# coding:utf-8
import scrapy


# 实例化浏览器可以通过process_response中的spider获取
# 实例化浏览器可以写在这里
class CarSpider(scrapy.Spider):
    name = "car2"
    # 这是一个可选的属性，包含了爬虫允许爬取的域名列表。当 OffsiteMiddleware 设置启用时，域名不在列表中的 URL 不会被跟进。
    # allowed_domain = ['dongchedi.com']
    start_urls = ['https://www.dongchedi.com/sales']

    def parse(self, response, **kwargs):

        filename = response.url.split("/")[-1] + '.txt'
        with open(filename, 'wb+') as f:
            i = 1
            while i < 3:
                name = response.xpath(
                    '/html/body/div[2]/main/div/div[1]/div[2]/a[1]/div/div[3]/p[' + str(i) + ']/text()').extract()
                i += 1
                print(name[0])
                try:
                    f.write(name[0].encode('utf-8'))
                    f.write(','.encode('utf-8'))
                except ValueError:
                    f.close()

