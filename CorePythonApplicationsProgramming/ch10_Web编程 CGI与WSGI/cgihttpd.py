# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : myhttpd.py.py
# Time       ：2021/1/8 11:32
# Author     ：author name
# version    ：python 3.7
# Description：简单的 CGIHTTPSERVER，提供了 do_HEAD，do_GET，do_POST方法
"""

from http.server import CGIHTTPRequestHandler, HTTPServer


def main():
	global server
	try:
		server = HTTPServer(('localhost', 8080), CGIHTTPRequestHandler)
		sa = server.socket.getsockname()
		serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
		print(serve_message.format(host=sa[0], port=sa[1]))
		print('Welcome to the machine... Press ^C once or twice to quit.')
		server.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		server.socket.close()

if __name__ == '__main__':
	main()
