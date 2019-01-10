#!/usr/bin/python
# #coding=utf-8
# nazo 登陆签到。还差判断  
import re
import urllib
import urllib.request
import sys
import requests
import json
from lxml import html
fordata = {
        'email':'821453880@qq.com',
        'passwd':'shishi4430',
        'remember_me':'week'
}
headr = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
url = 'https://www.nazoss.org/user/_login.php'

class MyError(Exception):
    msg=''
    def __init__(self,_msg):
        self.msg=_msg

s = requests.session() 
# https://www.nazoss.org/user/index.php
# https://www.nazoss.org/user/_checkin.php
def checkLogin(json):
        if json['code']!='1':
            raise MyError(_("Login failed,please check your password"))
def getConfigs():
    a = s.get('https://www.nazoss.org/user/all_node_json.php')
    print('getConfigs')
    print(a.json())
    return json.loads(a.text)
def indexnazo():
    a = s.get('https://www.nazoss.org/user/index.php')
    print('indexnazo')
    return json.loads(a.json())
def denglu():
    a = s.get('https://www.nazoss.org/user/_checkin.php')
    print('indexnazo')
    print(a.text)
    #return json.loads(a.json())
def doubb():
    #page = requests.get(url,cookies = cookie)
    #tree = html.fromstring(page.text)
    r = s.post(url, data=fordata)
    checkLogin(r.json())
    configList = getConfigs()
    for config in configList:
        config['id']=''
        config['remarks']=config['server']
        config['server_udp_port']=0
        config['udp_over_tcp']=False
    print(r.text)
    print('-------------------')
    print(r.json())
    print('-------------------')
    print(r.text)
    #indexnazo()
    denglu()

try:
    print("config has finished")
    print("hint:.........")
except MyError as e:
    print(e.msg)

doubb()