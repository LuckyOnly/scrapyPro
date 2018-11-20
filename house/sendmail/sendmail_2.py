# coding:utf-8

import smtplib
from email.mime.text import MIMEText
import os
import sys
from email.header import Header
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print rootPath

def sender():
    print '发送邮件'
    smtpHost = 'smtp.qq.com'
    sender = '1047670763@qq.com'
    password = "zmqlfm"
    # receiver = '525970280@qq.com'
    receiver = ['1047670763@qq.com','525970280@qq.com']

    f = open(rootPath+r"\model\mymssql\statistic_data1.json")
    line = f.readline()
    textr = []
    while line:
        textr.append(line)
        line = f.readline()

    body = ' '.join(textr)
    msg = MIMEText(body)

    msg['Subject'] = 'scrapy emails'
    msg['From'] = sender
    msg['To'] = Header(u"房产",'utf-8')

    ## smtp port 25
    smtpServer = smtplib.SMTP(smtpHost, 25)  # SMTP
    smtpServer.login(sender, password)
    smtpServer.sendmail(sender, receiver, msg.as_string())
    smtpServer.quit()
    print 'send success by port 25'

if __name__ =="__main__":
    sender()