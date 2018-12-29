# coding:utf-8

from mssql import MsSql
from logging import log
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def gener():
    print u'写入数据库'
    ms_sql = MsSql()
    cur = ms_sql.conn
    # cur.execute("SELECT * from info WHERE price!='待定' order by price asc")
    # cur.execute('SELECT * from department  ORDER BY substring_index(price,"元",1)+0 asc')
    # cur.execute('SELECT * from department  where substring_index(price,"元",1)+0 < 30000 ORDER BY substring_index(price,"元",1)+0 asc')
    cur.execute('SELECT * from department  where substring_index(price,"元",1)+0 < 30000 ORDER BY cdate desc')
    ms_sql.ms.close()
    try:
        with open(rootPath+r'\mymssql\statistic_data1.json','w+') as f:
            for data in cur.fetchall():
                for content in data:
                    f.write(str(content)+"  ")
                f.write('\n')
        f.close()
    except Exception as error:
        log(1,error)

if __name__ == "__main__":
    gener()