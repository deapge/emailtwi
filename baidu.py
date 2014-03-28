#!/usr/bin/python
# -*- encoding: utf8 -*-

# http://blog.chinaunix.net/uid-20196333-id-1972398.html
# http://www.2cto.com/kf/201306/223584.html

import sys
import re
import string
import httplib
import urllib2
import re
def StripTags(text):
    finished = 0
    while not finished:
        finished = 1
        start = text.find("<")
        if start >= 0:
            stop = text[start:].find(">")
            if stop >= 0:
                text = text[:start] + text[start+stop+1:]
                finished = 0
    return text
  
if len(sys.argv) != 2:
        print "\nrsx.py : Find hundreds of e-mail adresses on baidu.\n"
        print "\nUsage : ./baidu.py \n"
        print "\nexemple: ./baidu.py 163.com \n"
        sys.exit(1)
        
domain_name=sys.argv[1]
d={}
page_counter = 0

headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip,deflate,sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ru;q=0.2",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Host":"www.baidu.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
           }
try:
    while page_counter <100:
        url = "http://www.baidu.com/#wd="+str(domain_name)+"&tn=baidu&ie=utf-8&usm=2&rsv_bp=0&rsv_spt=3&rsv_sug3=5&rsv_sug4=187&rsv_sug1=5&rsv_sug2=0&inputT=4&pn="+repr(page_counter)
        request = urllib2.Request(url, headers = headers)
        text = urllib2.urlopen(request).read()
        print text
        emails = re.findall('([\w\.\-]+@'+domain_name+')',StripTags(text))
        print emails
        sys.exit()
        for email in emails:
            d[email]=1
            uniq_emails=d.keys()
        page_counter = page_counter +10
except IOError:
    print "No result found!"+""
page_counter_web=0


