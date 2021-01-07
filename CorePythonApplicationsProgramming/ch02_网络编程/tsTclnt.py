# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsTclnt.py.py
# Time       ：2021/1/7 19:45
# Author     ：author name
# version    ：python 3.7
# Description：TCP时间戳客户端：提示用户输入发送到服务端的消息，并接收从服服务端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。
"""

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input("> ")
	if not data:
		break
	tcpCliSock.send(data.encode("utf-8"))
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break
	print(data.decode("utf-8"))

tcpCliSock.close()
