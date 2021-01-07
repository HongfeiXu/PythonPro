# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsTclntSS.py.py
# Time       ：2021/1/7 20:45
# Author     ：author name
# version    ：python 3.7
# Description：这是一个时间戳TCP客户端，它知道如何与类似文件的SocketServer类StreamRequestHandler对象通信
"""


from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
	# SocketServer请求处理程序的默认行为是：接受连接，获取请求，然后关闭连接，
	# 所以不能在整个程序执行过程中都保持连接，需要在每次向服务器发送消息时，创建新的套接字
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = input("> ")
	if not data:
		break
	tcpCliSock.send(("%s\r\n" % data).encode("utf-8"))
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break
	print(data.decode("utf-8").strip())
	tcpCliSock.close()