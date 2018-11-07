# coding:utf-8

import smtplib
from email.mime.text import MIMEText

smtpHost = 'smtp.qq.com'
sender = '1047670763@qq.com'
password = "password"
receiver = '1047670763@qq.com'

# content = 'hello mimvp.com'
f = open("../model/mymssql/statistic_data.json")
line = f.readline()
textr = []
while line:
    textr.append(line)
    # line = f.readline().decode('unicode_escape')
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
