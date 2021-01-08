# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : myhttpd.py.py
# Time       ：2021/1/8 11:32
# Author     ：author name
# version    ：python 3.7
# Description：
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			f = open(self.path[1:], 'r')
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(f.read().encode("utf-8"))
			f.close()
		except IOError:
			self.send_error(404, 'File not found: %s' % self.path)


def main():
	global server
	try:
		server = HTTPServer(('', 80), MyHandler)
		print('Welcome to the machine... Press ^C once or twice to quit.')
		server.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		server.socket.close()

if __name__ == '__main__':
	main()
