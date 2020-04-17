# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:35:17 2020

@author: zsl
"""
import re
# 正则表达式
m = re.search(r'[1-9]\d{5}',"BIT 100081")
if m:
    print(m.group(0))

m = re.match(r'[1-9]\d{5}',"BIT 100081")
if m:
    print(m.group(0)) # 无结果
m = re.match(r'[1-9]\d{5}',"100081 BIT")
if m:
    print(m.group(0))

ls = re.findall(r'[1-9]\d{5}',"BIT100081 TSU100084")
ls # ['100081', '100084']

re.split(r'[1-9]\d{5}',"BIT100081 TSU100084") # ['BIT', ' TSU', '']
re.split(r'[1-9]\d{5}',"BIT100081 TSU100084",maxsplit=1) # ['BIT', ' TSU100084']

for m in re.finditer(r'[1-9]\d{5}',"BIT100081 TSU100084"):
    if m:
        print(m.group(0))
#100081
#100084
        
re.sub(r'[1-9]\d{5}','zipcode',"BIT100081 TSU100084") # 'BITzipcode TSUzipcode'

rst = re.search(r'[1-9]\d{5}',"BIT100081 TSU100084")
# 等价于
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search("BIT100081 TSU100084")

# match对象介绍
m = re.search(r'[1-9]\d{5}',"BIT100081 TSU100084")
m.string
m.re
m.pos
m.endpos
m.group(0)
m.start()
m.end()
m.span()