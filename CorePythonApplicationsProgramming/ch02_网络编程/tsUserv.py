# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsUserv.py.py
# Time       ：2021/1/7 20:18
# Author     ：author name
# version    ：python 3.7
# Description：UDP时间戳服务器：接收来自客户端发来的消息，将加了时间戳前缀的该消息返回给客户端
"""


from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print("waiting for message...")
	data, addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto(("[%s] %s" % (ctime(), data.decode("utf-8"))).encode("utf-8"), addr)
	print("...received from and returned to:", addr)

udpSerSock.close()
