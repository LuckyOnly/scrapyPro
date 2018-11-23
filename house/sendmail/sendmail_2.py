# coding:utf-8

import smtplib
import pandas as pd
from email.mime.text import MIMEText
import os
import sys
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf8')
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def convertToHtml(result,title):
    #将数据转换为html的table
    #result是list[list1,list2]这样的结构
    #title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

def get_data():
    f = open(rootPath+r'\model\mymssql\statistic_data1.json')
    line = f.readline()
    textr=[[u'序号',u'房屋名称',u'销售许可',u'单价',u'剩余套数',u'地址',u'开发商',u'物业',u'网址']]
    while line:
        a = line.strip().split('  ')
        textr.append(a)
        line = f.readline()
    return textr

def reverse_data():
    textr = get_data()
    L=[]

    for i in xrange(len(textr[0])):
        S = []
        for j in xrange(len(textr)):
            S.append(textr[j][i])
        L.append(S)
    return L

def sender():
    print '发送邮件'
    smtpHost = 'smtp.qq.com'
    sender = '1047670763@qq.com'
    password = "zmqlfm"
    # receiver = '525970280@qq.com'
    receiver = ['1047670763@qq.com','525970280@qq.com']



    result1 = reverse_data()
    title1=[]
    for i in  xrange(1,len(result1)+1):
        title1.append(str(i))
    data = convertToHtml(result1,title1)
    with open(rootPath+r'\model\mymssql\new.html','w+') as file:
        file.write("""<!DOCTYPE html>
                    <html lang="en" xmlns="http://www.w3.org/1999/html">
                        <head>
                            <meta charset="UTF-8">
                            <title>Title</title>
                        </head>
                            <body>"""
                   +data+"""</body></html>""")
        file.close()

    f = open(rootPath+r'\model\mymssql\new.html')
    line = f.readline()
    textr = []
    while line:
        textr.append(line)
        line = f.readline()
    body = ' '.join(textr)
    msg = MIMEText(body,"html","utf-8")

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