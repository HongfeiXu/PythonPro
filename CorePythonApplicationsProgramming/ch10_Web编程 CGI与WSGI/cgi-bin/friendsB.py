# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : friendsA.py.py
# Time       ：2021/1/12 9:50
# Author     ：author name
# version    ：python 3.7
# Description：friends.htm 和 friendsA.py 都合并进了 friendsB.py中。
最终的脚本可以用动态生成的HTML文件输出表单和返回页面。
浏览器访问：http://localhost:8080/cgi-bin/friendsB.py
"""

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''<html>
<meta charset="UTF-8">
<head><title>Friends CGI Demo</title></head>
<body><h3>Friends list for: <i>New User</i></h3>
<form action="/cgi-bin/friendsB.py">
<b>Enter your Name: </b>
<input type=hidden name=action value=edit>
<input type=text name=person value="NEW USER" size=15>
<p><b>How many friends do you have?</b>
%s
<p><input type=submit></form></body></html>'''

fradio = '<input type=radio name=howmany value="%s" %s> %s\n'


def showForm():
	friends = []
	for i in (0, 10, 25, 50, 100):
		checked = ''
		if i == 0:
			checked = 'checked'
		friends.append(fradio % (str(i), checked, str(i)))
	print('%s%s' % (header, formhtml % ''.join(friends)))


reshtml = '''<html>
<meta charset="UTF-8">
<head><title>Friends CGI Demo</title></head>
<body><h3>Friends list for: <i>%s</i></h3>
Your name is: <b>%s</b><p>
You have <b>%s</b> friends.
</body></html>'''


def doResults(who, howmany):
	print(header + reshtml % (who, who, howmany))


def process():
	form = cgi.FieldStorage()

	if 'person' in form:
		who = form['person'].value
	else:
		who = 'NEW USER'

	if 'howmany' in form:
		howmany = form['howmany'].value
	else:
		howmany = 0

	if 'action' in form:			# action变量决定显示那个页面（表单页面或结果页面）
		doResults(who, howmany)
	else:
		showForm()


if __name__ == '__main__':
	process()