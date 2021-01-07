# -*- coding: utf-8 -*-

# ----------------------------------
# Python super详解
# refs: https://km.netease.com/article/298856

# --------------
# 问题1（super的调用顺序问题）

class A1(object):
	def __init__(self):
		print("A1.__init__")
		super(A1, self).__init__()

class A2(A1):
	def __init__(self, s):
		print("A2.__init__ s= {}".format(s))
		super(A2, self).__init__()

class B(object):
	def __init__(self, s):
		print("B.__init__ s = {}".format(s))
		# super(B, self).__init__()		# traceback
		super(B, self).__init__(s)

class C(B, A2):
	def __init__(self, s):
		print("C.__init__ s = {}".format(s))
		super(C, self).__init__(s)

c = C("hello")

# 问题1：B的父类是object为啥super(B, self).__init__()，不传参数会报错？
# 分析：super的调用顺序是根据mro来的。mro已经有很多文章讲过了，这里不在多述。请看：Python多重继承分析

print(C.__mro__)		# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A2'>, <class '__main__.A1'>, <type 'object'>)

# 解决方法: 将参数s带上

# --------------
# 问题2（super调用细则问题）

class AA(object):
	def p(self):
		print("AA.p")

class BB(object):
	def p(self):
		print("BB.p")
		super(BB, self).p()

class CC(BB, AA):
	def p(self):
		print("CC.p")
		super(CC, self).p()

print("CC.__mro__ = {}".format(CC.__mro__))		# CC.__mro__ = (<class '__main__.CC'>, <class '__main__.BB'>, <class '__main__.AA'>, <type 'object'>)
cc = CC()
cc.p()
# CC.p
# BB.p
# AA.p

# 把B.p干掉，输出：
# CC.p
# AA.p

# 把B.p和A.p方法都干掉，报错：
# CC.p
# Traceback (most recent call last):
#   File "D:/Project/PythonPro/PythonDissect/Python super���.py", line 61, in <module>
#     cc.p()
#   File "D:/Project/PythonPro/PythonDissect/Python super���.py", line 57, in p
#     super(CC, self).p()
# AttributeError: 'super' object has no attribute 'p'

# super源码剖析，来理解问题2的原因

print(super.__doc__)

