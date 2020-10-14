#coding=utf-8

def singleton_decorator(cls, *args, **kwargs):
	"""
	单例装饰器
	"""
	instance = {}

	def wrap_singleton(*args, **kwargs):
		if cls not in instance:
			instance[cls] = cls(*args, **kwargs)
		return instance[cls]

	return wrap_singleton

@singleton_decorator
class MyLover(object):
	def __init__(self, my_lover):
		self._name = my_lover

	def get_name(self):
		print("我的老婆是：", self._name)


class MyGirl(object):
	def __init__(self, my_girl):
		self._name = my_girl

	def get_name(self):
		print("我的女票是：", self._name)

if __name__ == '__main__':
	m1 = MyLover("小美")
	m1.get_name()
	m2 = MyLover("小幂")
	m2.get_name()

	m1 = MyGirl("小美")
	m1.get_name()
	m2 = MyGirl("小幂")
	m2.get_name()

