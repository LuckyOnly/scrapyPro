from time import sleep
from scrapy.http import HtmlResponse
from selenium import webdriver

class CarreportsDownloaderMiddleware(object):
    def __init__(self):
        chrome_driver = r"F:\tools\Chrome-driver\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def process_response(self, request, response, spider):
        driver=self.driver
        # 如何动态加载数据
        # 使用spider获取获取浏览器对象
        print('返回新的响应对象')
        driver.get(url=request.url)
        # text = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[2]/a[1]/div/div[3]/p[1]').text
        # sleep(3)
        # print(text)
        sleep(3)
        page_text = driver.page_source
        return HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
