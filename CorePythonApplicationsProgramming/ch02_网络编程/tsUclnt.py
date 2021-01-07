# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsTclnt.py.py
# Time       ：2021/1/7 19:45
# Author     ：author name
# version    ：python 3.7
# Description：UDP时间戳客户端：提示用户输入发送到服务端的消息，并接收从服服务端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。
"""

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = input("> ")
	if not data:
		break
	udpCliSock.sendto(data.encode("utf-8"), ADDR)
	data, addr = udpCliSock.recvfrom(BUFSIZE)
	if not data:
		break
	print(data.decode("utf-8"))

udpCliSock.close()
