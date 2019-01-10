#!/usr/bin/python
# #coding=utf-8  
import re
import urllib
import urllib.request
import sys
import requests
from lxml import html
#还差密码登陆
#//*[@id="note_607451750_short"]/text()
#//*[@id="note_606616386_short"]/text()
#//span[@id="intro_display"]

cookies = {'source':'None',
           'redir':'https://www.douban.com/people/53052954/',
           'form_email':'821453880@qq.com',
           'form_password':'shishi4430',
           'login':'登录'}
#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400
headers = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
url_login = 'http://accounts.douban.com/login'
raw_cookies = 'ue="821453880@qq.com"; bid=gIXPpT8tDQU; ll="118281"; _ga=GA1.2.1374627703.1506153310; _vwo_uuid_v2=EA885C0667503631E047DB0A0DA8D15B|33783f7e236553153ae4670d940aff16; ct=y; ps=y; ue="821453880@qq.com"; dbcl2="53052954:gAu3efMCVws"; ck=58xD; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513414398%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D821453880%2540qq.com%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252Fpeople%252F132204190%252F%26source%3DNone%26error%3D1013%22%5D; __utmt=1; _pk_id.100001.8cb4=9b5193f788cca62e.1506153308.8.1513414416.1513254064.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1374627703.1506153310.1513253229.1513414399.20; __utmb=30149280.6.9.1513414416401; __utmc=30149280; __utmz=30149280.1513414399.20.17.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.5305; ap=1'
raw_cookies1 = 'bid=gIXPpT8tDQU; ll="118281"; _vwo_uuid_v2=EA885C0667503631E047DB0A0DA8D15B|33783f7e236553153ae4670d940aff16; ct=y; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1514107356%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D821453880%2540qq.com%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252Fpeople%252F132204190%252F%26source%3DNone%26error%3D1013%22%5D; _ga=GA1.2.1374627703.1506153310; _gid=GA1.2.425169977.1514107440; ue="821453880@qq.com"; dbcl2="53052954:yhR2FpY+QfU"; ck=jLdS; ap=1; __utmt=1; _pk_id.100001.8cb4=9b5193f788cca62e.1506153308.9.1514109050.1513415326.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1374627703.1506153310.1513414399.1514107356.21; __utmb=30149280.56.9.1514109049871; __utmc=30149280; __utmz=30149280.1513414399.20.17.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.5305'
cookie = {}
def doubb():
    for line in raw_cookies1.split(';'):
                key,value = line.split("=", 1)
                cookie[key] = value #一些格式化操作，用来装载cookies

    uil = 'https://www.douban.com/people/132204190/'
    page = requests.get(uil,cookies = cookie) #利用cookies登陆

    #page = requests.post(url_login ,data = cookies)
    tree = html.fromstring(page.text)
    intro_raw = tree.xpath('//span[@id="intro_display"]/text()') #//span[@id="intro_display"]/text()  //*[@id="intro_display"]
    
    #print(tree)

    print('-----------------------')
    f = open('douban_2.txt', 'wb+')
    #f.write(page.content)
    for i in intro_raw:
        intro = i.encode('utf-8')
        #f.write(intro) #page.content
        f.write(intro) 
        print(intro)
        

doubb()