#!/usr/bin/python
# #coding=utf-8
# nazo 登陆签到。还差判断  
import re
import urllib
import urllib.request
import sys
#import requests
import json
from lxml import html
from urllib import request

#url = 'https://www.baidu.com/'
#html = urllib.request.urlopen(url).read()
#html = html.decode('utf-8')
def getHtml(url):  
    html = urllib.request.urlopen(url).read()  
    return html  
  
def saveHtml(file_name,file_content):    
#    注意windows文件命名的禁用符，比如 /    
    with open (file_name.replace('/','_')+".html","wb") as f:  
#   写文件用bytes而不是str，所以要转码    
        f.write( file_content )

    print ("写入完成")
        
         
html = getHtml("http://tieba.baidu.com/p/2460150866")
#print(html)  
saveHtml("text1",html)  

print ("结束")  