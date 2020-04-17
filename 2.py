# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:11:21 2020

@author: zsl
"""
# 基本元素
import requests
from bs4 import BeautifulSoup 
url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
soup.a.name
tag = soup.a
tag.attrs
tag.attrs['class']
tag.attrs['href']
tag.string

# 属性
soup.head.contents #contents 是列表类型；.children,.descendants是迭代类型
for p in soup.a.parents:
    if p is None:
        print(p)
    else:
        print(p.name)
tag.next_siblings
tag.previous_siblings

# 更好输出
print(soup.prettify())

# 提取html里面所有的url链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 基于内容进行查找
soup.find_all(id = 'link')
import re
#正则表达式
soup.find_all(re.compile('link'))


# 中国大学排名爬取
import bs4
# 获取页面信息
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()# 如果不是200状态，就会引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
# 提取页面信息内容
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
#        children可能出现字符串类型，因此需要isinstance检查tr标签的类型
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    
    
# 打印内容,前num名大学信息
def printUnivList(ulist,num):
    #  {3}表示使用format中的第三个变量（中文字符）来填充
    #  解决中文输出排版问题
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    info=[]
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(info,html)
    printUnivList(info,20)
main()
   
    
    