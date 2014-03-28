#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
python adstwi 公共类
eg:发邮件
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.Header import Header

class AdsTwiCommon:
  EMAIL_FROM = 'deapge@163.com'
  EMAIL_TO   = ['978096002@qq.com']
  def __init__(self):
    pass
  
  def sendMail(self, log_path, subject = ''):
    '''
           发送 html 格式邮件
    '''
    mail_host    = "smtp.yeah.net"
    mail_user    = "gameguyz"
    mail_pass    = "gameguyz123"
    mail_postfix = "yeah.net"
    address      = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject, "UTF-8")
    msg['From']    = address
    msg['To']      = ";".join(self.EMAIL_TO)
    part = MIMEText(file(log_path).read(), 'html', _charset='UTF-8')
    msg.attach(part)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(address, self.EMAIL_TO, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
  common = AdsTwiCommon()
  print common.sendMail('templates/toptaobao-bak.htm', '测试邮件发送')
  pass
  