# coding:utf-8


from mssql import MsSql
from logging import log
def del_data():
    print "clear old data"
    ms_sql = MsSql()
    cur = ms_sql.conn
    try:
        # cur.execute("truncate table info")
        cur.execute("truncate table department")
        ms_sql.ms.close()
    except Exception as error:
        log('删除失败',error)

if __name__ == "__main__":
    del_data()