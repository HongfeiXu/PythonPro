# -*- coding: utf-8 -*-

# ----------------------------------
# Python多重继承分析
# refs: https://km.netease.com/article/297502

# python是支持多重继承的，但在多重继承背后还有两个重要的点需要说，也就是MRO(method resolution order)和super

# MRO算法的更迭：DFS->BFS->C3

# ------------
# super是一个对象，而非一个关键字

class A(object):
	def test(self):
		print("A.test")

a = A()
s = super(A, a)
print(s)		# <super: <class 'A'>, <A object>>
print(type(s))	# <class 'super'>

# ------------
# super的调用方式

class Base(object):
	def func(self):
		return "from Base"

class AA(Base):
	def func(self):
		return "from AA"

class BB(Base):
	def func(self):
		return "from BB"

class CC(AA, BB):
	def func(self):
		return "from CC"

cc_obj = CC()
print(super(CC, CC).func)		# <function AA.func at 0x000001DE9593B2F0>
print(super(CC, cc_obj).func)	# <bound method AA.func of <__main__.CC object at 0x000001DE95937A58>>
print(super(CC, CC).func(cc_obj))	# from AA
print(super(CC, cc_obj).func())		# # from AA

print(CC.__mro__)	# (<class '__main__.CC'>, <class '__main__.AA'>, <class '__main__.BB'>, <class '__main__.Base'>, <class 'object'>)


# ------------
# super的本质

class B(object):
	def test(self):
		print("B.test")
		super().test()

class C(B, A):
	def test(self):
		print("C.test")
		super().test()

c = C()
c.test()
# C.test
# B.test
# A.test

print(C.__mro__)		# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# 如结果，C实例调用test函数，现在C中打印，然后走到super会先调用父类的B的test，但是走到B中的test抵用super却调用了A的test，其中B和A不存在继承关系，这是为啥呢？
# 实际super不是针对调用父类而设计的，它的本质是在一个由一个或者多个类组成的有序集合中搜寻特定的类，并找到这个类中特定函数，
# 将一个实例绑定在这个函数上，生成一个bound method，并进行返回。而这个有序集合，就是类的mro。

# 除此，借由super，还能保证在此机制中公共父类只会被调用一次

class E(object):
	def __init__(self):
		print("EnterE")
		print("LeaveE")

class F(E):
	def __init__(self):
		print("EnterB")
		# super().__init__()
		super(F, self).__init__()	# 与上句等价
		print("LeaveB")

class G(E):
	def __init__(self):
		print("EnterG")
		super().__init__()
		print("LeaveG")

class H(F, G):
	def __init__(self):
		print("EnterH")
		super().__init__()
		print("LeaveH")

h = H()