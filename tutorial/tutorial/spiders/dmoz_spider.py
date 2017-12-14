import scrapy
class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domains=["dmoz.org"]
    start_urls=["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(selfself,response):
        filename=response.url.split("/")[-2]+'.html'
        with open(filename,'wd') as f:
            f.write(response.body)