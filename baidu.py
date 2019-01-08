#coding=utf-8
#!/usr/bin/python  
#百度贴吧下载图片
import re
import urllib
import urllib.request,sys
print('hello world')

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def down_gef(html):
    request = urllib.request.Request(html)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

def imgrealurl(url):
    reg1 = re.compile('(\w*\.jpg)') 
    imglist1 = re.findall(reg1,url)
    return imglist1

def getImg(html1):
    html1 = html1.decode('utf-8')     
    reg = re.compile('src="(.+?\.jpg)" pic_ext') 
    imglist = re.findall(reg,html1)
    x = 0
    pch = 'http://imgsrc.baidu.com/forum/pic/item/'
    print('***************************************') 
    for imgurl in imglist:
        img1 = down_gef(imgurl)
        print('--------------------------------------') 
        print(imgurl)
        imga1 =  imgrealurl(imgurl)
        str4 = "".join(imga1)
        savename = pch+str4
        #savename += imga1
        print(savename)
        urllib.request.urlretrieve(savename,'%s.jpg' % x)
        x+=1        
        
    #print(imglist)
    
html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html)
print('end-----')