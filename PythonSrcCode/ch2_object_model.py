#coding=utf-8

##################
# 一切皆对象

# 对象包括实例对象，类型对象

##################
# 类型对象体系

# a 是一个整数对象( 实例对象 )，其类型是整数类型( 类型对象 )
a = 1
print(type(a))				# <class 'int'>
print(isinstance(a, int))	# True

# 整数类型的类型还是一种类型，即 类型的类型
print(type(int))			# <class 'type'>

# object 是所有类型的基类
print(issubclass(type, object))	# True

# type是所有类型对象的类型
print(type(object))				# <class 'type'>

# 函数实例对象
def hel():
	pass

print(hel)					# <function hel at 0x0394A780>
print(type(hel))			# <class 'function'>
print(type(type(hel))) 		# <class 'type'>

print(issubclass(type(hel), object)) # True

class Dog(object):
	def yelp(self):
		print("woof")

dog = Dog()
print(type(dog))	# <class '__main__.Dog'>
print(type(Dog))	# <class 'type'>

# Dog的基类是 object
print(issubclass(Dog, object))	# True

class Sleuth(Dog):
	def hunt(self):
		pass

sleuth = Sleuth()
print(type(sleuth))	# <class '__main__.Sleuth'>
print(type(Sleuth))	# <class 'type'>

print(issubclass(Sleuth, Dog))		# True
print(issubclass(Sleuth, object))	# True

# object的类型是type，type的类型是type

print(type(object))
print(type(type))
print(type(type) is type)

# type的基类是object
print(issubclass(type, object))
print(type.__base__)

# object没有基类（对于存在继承关系的类，成员属性和成员方法查找需要回溯继承链，不断查找基类。 因此，继承链必须有一个终点，不然就死循环了。）
print(object.__base__)	# None

##################
# 对象只是名字

a = 1
print(id(a))
b = a
print(id(b))	# 与上面的输出一致

##################
# 可变对象 与 不可变对象

a = 1
print(id(a))
a += 1
print(id(a))
# 2073912496
# 2073912512

lst = [1, 2]
print(lst)
print(id(lst))
lst.append(3)
print(id(lst))
# 11290104
# 11290104


##################
# 定长对象 与 变长对象

import sys
print(sys.getsizeof(1))
print(sys.getsizeof(100000000000000000))
print(sys.getsizeof(100000000000000000000000000000000000000000000))
# 28
# 32
# 44

print(sys.getsizeof("a"))
print(sys.getsizeof("abc"))
# 50
# 52


print(sys.getsizeof(1.0))
print(sys.getsizeof(1000000000000000000000000000000000.0))
# 24
# 24

print(10. ** 1000)	# OverflowError: (34, 'Result too large')
