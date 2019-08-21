# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 15:50
# @Author  : Zhang
# @File    : 爬虫库--urllib.py

import urllib.request
import urllib.parse

url = "https://www.python.org"

resp = urllib.request.urlopen(url=url)

print(resp.status) # 获取状态码
print(resp.getheaders())  # 所有头信息
print(resp.getheader(name='Server')) # 对应的头信息
# print(resp.read().decode('utf-8')) # 读出整个网页

data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
resp = urllib.request.urlopen('http://httpbin.org/post',data=data)

print(resp.read())