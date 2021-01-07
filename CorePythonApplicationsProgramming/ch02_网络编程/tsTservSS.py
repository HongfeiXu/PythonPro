# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : tsTservSS.py.py
# Time       ：2021/1/7 20:38
# Author     ：author name
# version    ：python 3.7
# Description：SocketServer时间戳TCP服务器：通过使用SocketServer类、TCPServer和StreamRequestHandler，该脚本创建了一个时间戳服务器
"""


from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ""
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
	def handle(self) -> None:
		print ("...connected from:", self.client_address)
		self.wfile.write(("[%s] %s" % (ctime(), self.rfile.readline().decode("utf-8"))).encode("utf-8"))

tcpServ = TCP(ADDR, MyRequestHandler)
print("waiting for connection...")
tcpServ.serve_forever()
