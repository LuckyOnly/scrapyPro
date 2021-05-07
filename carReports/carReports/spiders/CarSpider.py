import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    # allowed_domain = ['dongchedi.com']
    start_urls = ['https://www.dongchedi.com/sales']

    def parse(self, response, **kwargs):
        # xpath获取车辆的信息
        for info in response.xpath('/html/body/div/main/div/div/div/a'):
            print(info)
            name = info.xpath('@href').extract()
            # name=response.xpath('/html/body/div[2]/main/div/div[1]/div[2]/a[1]/div/div[3]/p[2]/text()').extract()
            print(name)
        # filename = response.url.split("/")[-1]+'.txt'
        # print(filename)
        # with open(filename, 'wb') as f:
        #     for i in name:
        #         print(i)
        #         f.write(i)
