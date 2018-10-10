# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter

class HousePipeline(object):
    def __init__(self):
        self.file = open('house.json','wb')
        self.export = JsonItemExporter(self.file,encoding ='utf-8')
        self.export.start_exporting()
    def close_spider(self,spider):
        self.export.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        if item['title']:
            self.export.export_item(item)
            self.file.write('\n')
        return item
