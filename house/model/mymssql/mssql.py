# -*-coding:utf-8-*-
__author__ = 'JamesDing'
# *******************************************************************
#     Filename @  mssql.py
#       Author @  James
#  Create date @  2018/10/13 0013 10:55
#        Email @  zongff9095@163.com
#  Description @  邮件发送
#      license @ (C) Copyright 2011-2018, DevOps Corporation Limited.
# ********************************************************************


import MySQLdb
import sys
import ConfigParser
import os
reload(sys)
sys.setdefaultencoding('utf-8')
# get the database configure
cf = ConfigParser.ConfigParser()
path = os.path.dirname(os.path.abspath(__file__))
cf.read(path+r'\db1.cfg')
secs = cf.sections()
host = cf.get('db', 'host')
username = cf.get('db', 'username')
passwd = cf.get('db', 'passwd')
database = cf.get('db', 'database')
port = int(cf.get('db', 'port'))


class MsSql:

    def __init__(self):
        self.ms = MySQLdb.connect(host=host, port= port, user=username, passwd=passwd, db=database, charset= 'utf8')
        self.conn = self.ms.cursor()

    def query(self):
        cur = self.conn
        cur.execute('select * from info')
        for data in cur.fetchall():
            print data
        self.ms.close()
    def int_data(self):
        item = {'cdate': [u'2018-10-17'], 'link': 'http://www.njhouse.com.cn/2016/spf/detail.php?prjid=108689', 'name': [u'\u6e56\u5149\u5c71\u8272\u8857\u533a'], 'address': [u'\u6c5f\u5b81\u533a\u8c37\u91cc\u8857\u9053\u60a6\u6e56\u8def16\u53f7'], 'price': [u'22671\u5143/m'], 'manager': [u'\u5e7f\u4e1c\u78a7\u6842\u56ed\u7269\u4e1a\u670d\u52a1\u80a1\u4efd\u6709\u9650\u516c\u53f8'], 'unsale': [u' 60\u5957 '], 'engineer': [u'\n      \u5357\u4eac\u91d1\u68a6\u90fd\u623f\u5730\u4ea7\u5f00\u53d1\u6709\u9650\u8d23\u4efb\u516c\u53f8    ']}
        print str(item['name'][0])

        ms.conn.execute("insert into department(name,cdate,price,unsale,address,engineer,manager,link) values (%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'][0],item['cdate'][0],item['price'][0],item['unsale'][0],item['address'][0],item['engineer'][0].strip(),item['manager'][0],item['link']))

        self.ms.commit()
        self.ms.close()
if __name__=='__main__':
    ms = MsSql()
    ms.int_data()
    # ms.query()
    # print ur'\u77f3\u6797\u4e91\u57ce'

