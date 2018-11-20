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
        self.file = open('house1.json','wb')
        self.export = JsonItemExporter(self.file,encoding ='utf-8')
        self.export.start_exporting()
    def close_spider(self,spider):
        self.export.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        ms_sql = MsSql()
        self.export.export_item(item)
        self.file.write('\n')
        if "0套" not in item['unsale'][0]:
            try:
                ms_sql.conn.execute(
                     "insert into department(name,cdate,price,unsale,address,engineer,manager,link) values (%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'][0],item['cdate'][0],item['price'][0],item['unsale'][0],item['address'][0],item['engineer'][0].strip(),item['manager'][0],item['link']))
                ms_sql.ms.commit()
            except Exception as error:
                log(1,error)
        return item
