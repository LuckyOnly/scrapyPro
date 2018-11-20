# coding:utf-8

import os
import sys
# 添加当前项目的绝对地址
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from house.model.mymssql.generate_data2 import gener
from house.sendmail.sendmail_2 import sender




# 写入数据库
gener()
#发送邮件
sender()