# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsTserv.py.py
# Time       ：2021/1/7 10:58
# Author     ：author name
# version    ：python 3.7
# Description：TCP时间戳服务器：创建一个TCP服务器，然后将消息加上时间戳并发送回客户端
"""


from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print("waiting for connection...")
	tcpCliSock, addr = tcpSerSock.accept()	# 阻塞
	print("...connected from: ", addr)

	while True:
		data = tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		tcpCliSock.send(("[%s] %s" % (ctime(), data.decode("utf-8"))).encode("utf-8"))
	tcpCliSock.close()

tcpSerSock.close()
