# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : urlopen_test.py.py
# Time       ：2021/1/11 17:23
# Author     ：author name
# version    ：python 3.7
# Description： 开启myhttpd服务器后，访问之，读取文本
"""
from urllib.request import urlopen, urlretrieve

URL = "http://localhost/x.html"
f = urlopen(URL)
line = f.readline()
while line:
	print(line.decode("utf-8"))
	line = f.readline()
