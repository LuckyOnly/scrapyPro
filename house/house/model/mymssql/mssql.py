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

# import pymssql
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

host = '127.0.0.1'
username = 'root'
passwd = 'root'
database = 'house'
port=3306

class MsSql:
    def __init__(self):
        # self.ms = pymssql.connect(host=host,port= port,user=username,password=passwd,database=database)
        self.ms = MySQLdb.connect(host=host,port= port,user=username,passwd=passwd,db=database,charset = 'utf8')
        self.conn =self.ms.cursor()
    def query(self):
        cur = self.conn
        cur.execute('select * from info')
        for data in cur.fetchall():
            print  data
    def int_data(self):
        item = {'status': u'\u5728\u552e', 'type': u'\u4f4f\u5b85', 'price': u'25000\u5143/\u33a1', 'link': 'http://newhouse.nj.house365.com/shilinyuncheng/', 'title': [u'\u77f3\u6797\u4e91\u57ce']}
        ms.conn.execute("insert into info(title,price,type,status,link) values (%s,%s,%s,%s,%s)",(item['title'][0], item['price'], item['type'], item['status'], item['link']))

        self.ms.commit()
if __name__=='__main__':
    ms = MsSql()
    # ms.int_data()
    ms.query()

