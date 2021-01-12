# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : friendsA.py.py
# Time       ：2021/1/12 9:50
# Author     ：author name
# version    ：python 3.7
# Description：CGI脚本从 friends.htm 表单中获取person和howmany字段，使用这些数据创建动态生成的结果页面
浏览器访问：http://localhost:8080/friends.htm
"""

import cgi
import cgitb


reshtml ="""Content-Type: text/html\n
<HTML>
    <meta charset="UTF-8">
    <HEAD>
        <TITLE>Friends CGI Demo (dynamic screen)</TITLE>
    </HEAD>
    <BODY>
        <H3>Friends list for: <I>%s</I></H3>
        <P>Your name is: <B>%s</B>
        <P>You have <B>%s</B> friends.
    </BODY>
</HTML>
"""

form = cgi.FieldStorage()
who = form["person"].value
howmany = form["howmany"].value
print(reshtml % (who, who, howmany))