#coding=utf-8

# ============================
# type()
# 既可以查看一个类型或变量的类型，也可以创建出新的类型
# refs: https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072


class Hello(object):
	def hello(self, name="world"):
		print("Hello, %s" % name)


# 用type函数创建新的类型
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

def fn(self, name="world"):
	print("Hello2, %s" % name)

Hello2 = type("Hello2", (object,), dict(hello2=fn))	# 用type创建Hello2 class


#====测试代码====

# if __name__ == '__main__':
# 	h = Hello()
# 	h.hello()
# 	print type(Hello)
# 	print type(h)
#
# 	h2 = Hello2()
# 	h2.hello2()
# 	print type(Hello2)
# 	print type(h2)

# ============================
# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 元类->类->实例


# metaclass 是类的模板，所以必须从type类派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs["add"] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)


"""
当我们传入关键字参数metaclass时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
"""
class MyList(list, metaclass=ListMetaclass):
	pass


#====测试代码====

if __name__ == '__main__':
	L = MyList()
	L.add(1)
	print(L)


# 总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。 “Object Relational Mapping”
# 让我们来尝试编写一个ORM框架。

# 见 orm.py