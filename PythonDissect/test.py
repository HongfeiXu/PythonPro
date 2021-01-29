# -*- coding: utf-8 -*-


class A1(object):
	def __init__(self):
		print 'A1.__init__'
		super(A1, self).__init__()

class A2(A1):
	def __init__(self, s):
		print 'A2.__init__ s=', s
		super(A2, self).__init__()

class B(object):
	def __init__(self, s):
		print 'B.__init__ s=', s
		super(B, self).__init__()

class C(B, A2):
	def __init__(self, s):
		print 'C.__init__ s=', s
		super(C, self).__init__(s)

c = C('hello')