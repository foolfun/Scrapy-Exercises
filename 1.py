# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:10:40 2020

@author: zsl
"""
import requests
import time

#一般爬取网站内容
def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()#如果不是200状态，就会引发HTTPError异常
        r.encoding = r.apparent_encoding
#        print(r.raise_for_status())
        return r.text
    except:
        return "异常"

url="https://www.baidu.com"
start_time = time.time()
for i in range(100):
    tex = getHtml(url)
#    print(tex)
end_time = time.time()
print('total time is ',end_time-start_time)        

#对于亚马逊的爬取，需要模拟浏览器
kv = {'user-agent':'Mozilla/5.0'}
url = "http://www.amazon.cn/gp/product/B01M8L5Z3Y"
r = requests.get(url,headers = kv)
r.status_code
r.request.headers

#对百度搜索关键词python爬取信息
kv = {'wd':'python'}
url = "http://www.baidu.com"
r = requests.get(url,headers = kv)
len(r.text)

#爬取图片
import os
root = 'D://'
url = "http://i0.hdslb.com/bfs/article/12d0f8f7f289cd4beb2787b6ddeba953d57dbe30.jpg"
r = requests.get(url)
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    elif not os.path.exists(path):
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('save!')
    else:
        print('文件已经存在')
except:
    print('fail')

#ip地址查询
import requests
url = 'http://m.ip138.com/ip.asp?ip='
r = requests.get(url+'202.204.80.112')
r.status_code
r.text[-500:]

    