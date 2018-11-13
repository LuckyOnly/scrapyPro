# coding:utf-8

import smtplib
from email.mime.text import MIMEText
import os

def sender():
    print '发送邮件'
    smtpHost = 'smtp.qq.com'
    sender = '1047670763@qq.com'
    password = "zmqlfm"
    # receiver = '525970280@qq.com'
    receiver = '1047670763@qq.com'

    path_1 = os.path.dirname(os.getcwd())
    f = open(path_1+r"\house\model\mymssql\statistic_data.json")
    line = f.readline()
    textr = []
    while line:
        textr.append(line)
        line = f.readline()

    body = ' '.join(textr)
    msg = MIMEText(body)

    msg['Subject'] = 'scrapy emails'
    msg['From'] = sender
    msg['To'] = receiver

    ## smtp port 25
    smtpServer = smtplib.SMTP(smtpHost, 25)  # SMTP
    smtpServer.login(sender, password)
    smtpServer.sendmail(sender, receiver, msg.as_string())
    smtpServer.quit()
    print 'send success by port 25'

if __name__ =="__main__":
    sender()