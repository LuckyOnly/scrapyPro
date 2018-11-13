# coding:utf-8

from mssql import MsSql
from logging import log
def gener():
    print '写入数据库'
    ms_sql = MsSql()
    cur = ms_sql.conn
    cur.execute(
        "SELECT * from info WHERE price!='待定' order by price asc")
    ms_sql.ms.close()
    try:
        with open('statistic_data.json','w') as f:
            for data in cur.fetchall():
                for content in data:
                    f.write(str(content))
                f.write('\n')
        f.close()
    except Exception as error:
        log('写入文件出错',error)

if __name__ == "__main__":
    gener()