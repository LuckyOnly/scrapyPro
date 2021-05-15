import scrapy
from tutorial.items import DmozItem
# from tutorial.tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domains=["dmoz.org"]
    start_urls=["http://www.dmoz.org/Computers/Programming/Languages/Python"]


    def parse(self,response):
        for href in response.css("ul.directory.dir-col>li>a::attr('href')"):
            url=response.urljoin(response.url,href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)
    def parse_didr_contents(selfself,response):
        # filename=response.url.split("/")[-2]+'.html'
        # with open(filename,'wd') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul/li'):
            item=DmozItem()
            item['title']=sel.xpath('a/text()').extract()
            item['link']=sel.xpath('a/@href').extract()
            item['desc']=sel.xpath('text()').extract()
            print(item)




            #scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"