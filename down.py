#!/usr/bin/env python
#coding=utf-8 

import smtplib
import httplib
import urllib
import re
import csv
import sys
import time
import codecs
import json
import threading
import  copy
import datetime
import sys

#http://dwd7slh0nmufg.cloudfront.net/img/products/AK-003-1508-10435_p01_160.jpg

start=1
end=10000

conn = httplib.HTTPConnection("dwd7slh0nmufg.cloudfront.net")  
f=codecs.open('images.html','w', 'utf-8')

def down(no):
    conn.request('GET', '/img/products/AK-003-1509-%d_p01_160.jpg'%no)  
    r = conn.getresponse()
    #if r.status!=200: return
    t=r.read()
    if len(t)>1000:
        print 'no=%d'%(no)
        print >>f,'<img src="http://dwd7slh0nmufg.cloudfront.net/img/products/AK-003-1509-%d_p01_160.jpg" width=160px hight=160px />' %no

i=start
while i<=end:
    down(i)
    i=i+1