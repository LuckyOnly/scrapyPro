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
        item = {'status': u'\u5728\u552e', 'type': u'\u4f4f\u5b85', 'price': u'25000\u5143/\u33a1', 'link': 'http://newhouse.nj.house365.com/shilinyuncheng/', 'title': [u'\u77f3\u6797\u4e91\u57ce']}
        print str(item['title'][0])
        ms.conn.execute("insert into info(title,price,type,status,link) values (%s,%s,%s,%s,%s)",(str(item['title'][0]), item['price'], item['type'], item['status'], item['link']))

        self.ms.commit()
        self.ms.close()
if __name__=='__main__':
    ms = MsSql()
    # ms.int_data()
    # ms.query()
    # print ur'\u77f3\u6797\u4e91\u57ce'

