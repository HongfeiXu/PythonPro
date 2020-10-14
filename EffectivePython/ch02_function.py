# -*- coding: utf-8 -*-

import os

# 第二章 函数

#--------------------------------------
# 第14条：尽量用异常来表示特殊情况，而不要返回None

def divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return None

# 如果None这个返回值，对函数有特殊意义，那在编写Python代码来调用该函数时，就容易犯这里的错误
x, y = 0, 5
result = divide(x, y)
if not result:
	print "Invalid inputs"	# This is wrong!

# 比较好的方式是不返回None，将异常抛给上一级，使得调用者必须应对它

def divide_2(a, b):
	try:
		return a / b
	except ZeroDivisionError as e:
		raise ValueError(e)

x, y = 5, 3
try:
	result = divide_2(x * 1.0, y)
except ValueError:
	print "Invalid inputs"
else:
	print "Result is {:.2}".format(result)

#--------------------------------------
# 第15条：了解如何在闭包里使用外围作用域中的变量

# 例子：有一份列表，其中的元素都是数字，现在要对其排序，但排序时，要把出现在某个群组内的数字，放在群组外数字之前

def sort_priority(values, group):
	def helper(x):
		if x in group:
			return (0, x)
		return (1, x)
	values.sort(key = helper)	# helper函数的返回值（排序关键字），将会用来决定列表中各元素的顺序

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers, group)
print "---sort_priority---"
print numbers

# 上述函数之所以能正常运作，是因为：
# 1. Python支持闭包(closure)：闭包是一种定义在某个作用域中的函数，这种函数引用了那个作用域里的变量
# 2. Python函数是一级对象(first-class object)：我们可以直接引用函数、把函数赋给变量、把函数当成参数传给其他函数、并通过表达式及if对其进行比较和判断
# 3. Python使用特殊的规则来比较两个元组

# 如果这个sort_priority函数返回一个值，表示用户界面里是否出现了优先级较高的元件就更好了

# 试试如下写法：

def sort_priority2(values, group):
	found = False				# Scope: "sort_priority2"
	def helper(x):
		if x in group:
			found = True		# Scope: "helper" -- Bad!
			return (0, x)
		return (1, x)
	values.sort(key = helper)
	return found

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
found = sort_priority2(numbers, group)
print "---sort_priority2---"
print numbers
print found	# False

# 注1：表达式中引用变量时，Python解释器按如下顺序遍历各个作用域，以解析该引用：
# 1. 当前函数的作用域
# 2. 任何外围作用域（如，包含当前函数的其他函数）
# 3. 包含当前代码的那个模块的作用域（全局作用域）
# 4. 内置作用域（也就是包含len及str等函数的那个作用域）
# 如果上面这些地方都没有定义过名称相符的变量，就抛出NameError异常

# 注2：给变量赋值时，规则有所不同
# 如果当前作用域已经定义了这个变量，那么该变量就会具备新值；
# 如果当前作用域没有这个变量，Python会把这次赋值视为对该变量的定义，而新定义的这个变量，其作用域就是包含赋值操作的这个函数

# 注3：Python是故意这么设计，可以防止函数中的局部变量污染函数外的那个模块

# 获取闭包数据

# Python3中可使用nonlocal语句

# 也可将相关状态封装为辅助类(helper class)

class Sorter(object):
	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sorter = Sorter(group)	# 辅助对象
numbers.sort(key=sorter)
print "---Sorter---"
print numbers
print sorter.found

# Python2中的值
# Python2中不支持nonlocal关键字
# 可以利用Python的作用域规则来解决，虽然不优雅，但已经成为一种Python编程习惯

def sort_priority3(values, group):
	found = [False]		# mutable，包含单个元素的列表
	def helper(x):
		if x in group:
			found[0] = True
			return (0, x)
		return (1, x)
	values.sort(key = helper)
	return found

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
found = sort_priority3(numbers, group)
print "---sort_priority3---"
print numbers
print found

#--------------------------------------
# 第16条：考虑用生成器来改写直接返回列表的函数

# 例子：查出字符串中每个词的首字母在整个字符串中的位置

def index_words(text):
	result = []
	if text:
		result.append(0)
	for index, letter in enumerate(text):
		if letter == ' ':
			result.append(index+1)
	return result

address = "Four score and seven years ago..."
result = index_words(address)
print result[:3]

# 用生成器来改写

def index_words_iter(text):
	if text:
		yield 0
	for index, letter in enumerate(text):
		if letter == " ":
			yield index+1

result = list(index_words_iter(address))
print result[:3]

# 下面这个生成器，从文件里面依次读入各行内容，然后逐个处理每行中的单词，并产生相应的结果
# 该函数执行所消耗的内存，由单行输入值的最大字符数来界定

def index_file(handle):
	offset = 0
	for line in handle:
		if line:
			yield offset
		for letter in line:
			offset += 1
			if letter == " ":
				yield offset

with open("address.txt", "r") as f:
	it = index_file(f)
	print next(it)
	print next(it)

#--------------------------------------
# 第17条：在参数上面迭代时，要多加小心

# 例子：求出每个城市有游客数量百分比

def normalize(numbers):
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100.0 * value / total
		result.append(percent)
	return result

visits = [15, 35, 80]
percentages = normalize(visits)
print percentages

# 扩大函数应用范围，把Texas每个城市的游客数放在文件中，定义生成器函数来读取每行数据

def read_visits(data_path):
	with open(data_path) as f:
		for line in f:
			yield int(line)

it = read_visits("my_numbers.txt")
percentages = normalize(it)
print percentages	# [] ！！！

# 注：出现这种情况的原因在于，迭代器只能产生一轮结果；在抛出过StopIteration异常的迭代器或生成器上面继续迭代第二轮，是不会有结果的

it = read_visits("my_numbers.txt")
print list(it)	# [15, 35, 80]
print list(it)	# []

# 为了解决这个问题，可以用该迭代器制作一份列表，然后操作该列表


def normalize_copy(numbers):
	numbers = list(numbers)		# Copy the iterator
	total =sum(numbers)
	result = []
	for value in numbers:
		percent = 100.0 * value / total
		result.append(percent)
	return result

percentages = normalize(visits)
print percentages

# 注，上面这种写法的问题在于，待复制的那个迭代器可能包含大量数据，导致内存崩溃
# 一种解决办法是，通过参数来接受另外一个函数，那个函数每次调用后，都能返回新的迭代器

def normalize_func(get_iter):
	total =sum(get_iter())
	result = []
	for value in get_iter():
		percent = 100.0 * value / total
		result.append(percent)
	return result

percentages = normalize_func(lambda : read_visits("my_numbers.txt"))
print percentages

# 还有更好的方法，达到同样的效果，即，编写一种实现迭代器协议的容器类（iterator protocol）
# Python在for循环便利容器时，就是依靠这个迭代器协议，for x in foo，实际上回调用iter(foo)，实际上调用foo.__iter__，
# 此方法必须返回迭代器对象，而那个迭代器本身，则实现了名为__next__的特殊方法

# 简单来说，就是要令自己的类把__iter__方法实现为生成器
# 下面，定义一个可以的迭代的容器类

class ReadVisits(object):
	def __init__(self, data_path):
		self.data_path = data_path

	def __iter__(self):
		with open(self.data_path) as f:
			for line in f:
				yield int(line)

visits = ReadVisits("my_numbers.txt")	# 这个容器类可以传给原来的normalize函数，无需再做修改
percentages = normalize(visits)			# normalize函数中的sum方法会调用ReadVisits.__iter__，得到新的迭代器对象；
										# 而for循环也会调用__iter__得到另一个新的迭代器对象，互补影响
print percentages

# 修改normalize函数，以确保调用者传进来的参数不是迭代器对象本身
# 利用iter函数的行为进行判断：若传入迭代器对象，则返回该迭代器；若传入的是容器类型对象，则返回新的迭代器对象

def normalize_defensive(numbers):
	if iter(numbers) is iter(numbers):	# An iterator -- bad!
		raise TypeError("Must supply a container")
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100.0 * value / total
		result.append(percent)
	return result

visits = [15, 35, 80]
normalize_defensive(visits)				# No error
visits = ReadVisits("my_numbers.txt")
normalize_defensive(visits)				# No error

it = iter(visits)
try:
	normalize_defensive(it)
except TypeError as e:
	print e
# Must supply a container

#--------------------------------------
# 第18条：用数量可变的位置参数减少视觉杂讯（visual noise）

def log(message, values):
	if not values:
		print message
	else:
		values_str = ", ".join(str(x) for x in values)
		print "{}: {}".format(message, values_str)

log("My numbers are", [1, 2])
log("Hi there", [])	# ugly

def log2(message, *values):
	print type(values)	# <type 'tuple'>
	if not values:
		print message
	else:
		values_str = ", ".join(str(x) for x in values)
		print "{}: {}".format(message, values_str)

log2("My numbers are", 1, 2)
log2("Hi there")

favorites = [7, 33, 99]
log2("Favorite colors", *favorites)	# 加上*，则Python将列表中的元素视为位置参数

# 接受数量可变的位置参数，会带来两个问题：
# 1. 变长参数传给函数时，总是要先转化为元组，如果传入的是带有*操作符的生成器，
# 则Python就必须把该生成器完整迭代一轮，放入元组中，可能消耗大量内存，导致崩溃

def my_generator():
	for i in xrange(10):
		yield i

def my_func(*args):
	print args

it = my_generator()
my_func(*it)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 注：只有当我们能够确定输入的参数个数比较少时，才应该令函数接受*args式的边长参数

# 2. *args参数的第二个问题是，如果以后给函数添加新的位置参数，就必须修改调用该函数的那些旧代码，否则会产生难以调试的错误

def log3(sequence, message, *values):	# log3 为 log2 的新版本
	if not values:
		print "{}: {}".format(sequence, message)
	else:
		values_str = ", ".join(str(x) for x in values)
		print "{}: {}: {}".format(sequence, message, values_str)

log3(1, "Favorites", 7, 33)		# New usage is OK
log3("Favorites", 7, 33)		# Old usage breaks
# Favorites: 7: 33， 不是期望的结果，但没有报错

# 注：为了避免此种情况，我们应该使用只能以关键字形式指定的参数来扩展这种接收接受*args的函数，见第21条

#--------------------------------------
# 第19条：用关键字参数来表达可选的行为
# 注：位置参数必须出现在关键字参数前面

def remainder(number, divisor):
	return number % divisor

assert remainder(20, 7) == 6

# 好处1，代码易读
# 好处2，可在函数定义中提供默认值

def flow_rate(weight_diff, time_diff, period=1):
	return (weight_diff / time_diff) * period

# 好处3，提供了一种扩充函数参数的有效方式，扩充后的函数依然能与原有的那些调用代码兼容

def flow_rate_2(weight_diff, time_diff, period=1, units_per_kg=1):
	return (weight_diff * units_per_kg/ time_diff) * period

# 注：以位置参数的形式来指定可选参数，是容易令人困惑的，建议，一直以关键字形式来指定这些参数
# pounds_per_hour = flow_rate_2(weight_diff, time_diff, 3600, 2.2)							# Bad
# pounds_per_hour = flow_rate_2(weight_diff, time_diff, period=3600, units_per_kg=2.2)		# Good

#--------------------------------------
# 第20条：用None和文档字符串来描述具有动态默认值的参数

# 需求：有时我们想采用一种非静态的类型，来作为参数的默认值

from time import asctime, sleep
def logg(message, when=asctime()):
	print "{}: {}".format(when, message)

logg("Hi, there!")
sleep(1)
logg("Hi, again!")
# Fri Jan 10 17:46:48 2020: Hi, there!
# Fri Jan 10 17:46:48 2020: Hi, again!

# 这里发现，两个时间戳一样，因为asctime()在函数定义时执行了一次，之后就固定不变了
# 原因：参数的默认值，只会在程序加载模块并读到本函数的定义时评估一次，对于{}或[]等动态的值，可能会导致奇怪的行为
# 在Python中若想正确实现动态默认值，习惯上是把默认值设为None，并注释描述

def loggg(message, when = None):
	"""
	Log a message with timestamp
	:param message:
	:param when: datetime of when the message occurred. Defaults to the present time.
	:return:
	"""
	when = asctime() if when is None else when
	print "{}: {}".format(when, message)

loggg("Hi, there!")
sleep(1)
loggg("Hi, again!")

# Fri Jan 10 17:55:03 2020: Hi, there!
# Fri Jan 10 17:55:04 2020: Hi, again!

# 如果参数的实际默认值是可变类型（mutable），那么就一定要记得用None作为形式上的默认值
# 例子：从编码为JSON格式的数据中载入某个值，若失败，则默认返会空的字典

import json

def decode(data, default={}):
	try:
		return json.loads(data)
	except ValueError:
		return default

foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print "foo = {}".format(foo)
print "bar = {}".format(bar)
# 结果如下，可见foo和bar都等同于写在default中的那个字典
# foo = {'stuff': 5, 'meep': 1}
# bar = {'stuff': 5, 'meep': 1}

# 解决办法如下

def decode2(data, default=None):
	"""
	Load Json data from a string
	Args:
		data: JSON data to decode
		default: Value to return if decoding fails.
			Defaults to an empty dicitionary.
	:param data:
	:param default:
	:return:
	"""
	if default is None:
		default = {}
	try:
		return json.loads(data)
	except ValueError:
		return default

foo = decode2("bad data")
foo["stuff"] = 5
bar = decode2("also bad")
bar["meep"] = 1
print "foo = {}".format(foo)
print "bar = {}".format(bar)

# foo = {'stuff': 5}
# bar = {'meep': 1}

#--------------------------------------
# 第21条：用只能以关键字形式指定的参数来确保代码明晰

# 这里展示Python2的实现方法，Python3有更简单的方式

def print_args(*args, **kwargs):
	print "Positional: ", args	# args 用来接受数量可变的位置参数
	print "Keyword: ", kwargs	# kwargs用来接受任意数量的关键字参数

print_args(1, 2, foo="bar", stuff="meep")

def safe_division_d(number, divisor, **kwargs):
	ignore_overflow = kwargs.pop("ignore_overflow", False)		# 取走关键字参数，若无，则返回默认参数False
	ignore_zero_div = kwargs.pop("ignore_zero_division", False)
	if kwargs:	# 防止无效的参数值，抛出TypeError异常
		raise TypeError("Unexcepted **kwargs: %r" % kwargs)
	try:
		return number / divisor
	except OverflowError:
		if ignore_overflow:
			return 0
		else:
			raise
	except ZeroDivisionError:
		if ignore_zero_div:
			return float("inf")
		else:
			raise

safe_division_d(1.0, 10**500, ignore_overflow=True)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10)
# safe_division_d(1, 0, False, True)		# 错误，只能以关键字形式指明参数
# safe_division_d(0, 0, unexcepted=True)	# 错误，传入了无效参数










