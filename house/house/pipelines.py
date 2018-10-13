# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
from model.mymssql.mssql import MsSql
from logging import log

class HousePipeline(object):
    def __init__(self):
        self.file = open('house.json','wb')
        self.export = JsonItemExporter(self.file,encoding ='utf-8')
        self.export.start_exporting()
    def close_spider(self,spider):
        self.export.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        ms_sql = MsSql()
        if item['title'] and item['type'] == u'住宅':
            if item['status'] in [u'新盘',u'尾盘',u'在售']:
                self.export.export_item(item)
                self.file.write('\n')
                try:
                    ms_sql.conn.execute(
                         "insert into info(title,price,type,status,link) values (%s,%s,%s,%s,%s)",(item['title'][0],item['price'],item['type'],item['status'],item['link']))
                    ms_sql.ms.commit()
                except Exception as error:
                    log(1,error)
        return item
