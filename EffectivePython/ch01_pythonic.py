# -*- coding: utf-8 -*-

import os

# 第一章 用Pythonic方式来思考

#--------------------------------------
# 第1条：确认自己所使用的Python版本
# import this

#--------------------------------------
# 第2条：遵循PEP 8风格指南

# if not a is b		坏
# if a is not b		好

# if len(somelist) == 0		坏
# if not somelist			好

# 不要编写单行的if语句、for循环、while循环、except复合语句

# import 放在文件开头

# 引入模块时，使用绝对名称

# import语句分为三个部分：标准库模块、第三方模块、自用模块，每部分中，按照模块的字母顺序排列

#--------------------------------------
# 第3条：了解bytes、str与unicode的区别

# Python3: bytes, str

# Python2: str, unicode

def to_unicode(unicode_or_str):
	if isinstance(unicode_or_str, str):
		value = unicode_or_str.decode("utf-8")
	else:
		value = unicode_or_str
	return value	# Instance of unicode

def to_str(unicode_or_str):
	if isinstance(unicode_or_str, unicode):
		value = unicode_or_str.encode("utf-8")
	else:
		value = unicode_or_str
	return value	# Instance of str

# 注：Python2 中，若str只包含7位ASCII字符，则unicode和str实例似乎就成了同一种类型
# 可以用+号连接这种str与unicode
# 可以用等价与不都能加操作符
# 可以用'%s'等形式来代表unicode实例

with open("random.bin", "w") as f:
	f.write(os.urandom(10))

#--------------------------------------
# 第4条：用辅助函数来取代复杂的表达式

def get_first_int(values, key, default=0):
	found = values.get(key, [""])
	if found[0]:
		found = int(found[0])
	else:
		found = default
	return found

#--------------------------------------
# 第5条：了解切割序列的办法

a = [1,2,3]
b = a[:]
assert b == a and b is not a	# 原列表的拷贝

b = a
print "Before {}".format(a)
a[:] = [101, 102, 103]
assert a is b				# Still the same list object
print "After {}".format(a)	# Now has different contents

#--------------------------------------
# 第6条：在单次切片操作内，不要同时指定start、end和stride

a =  ["red", "orange", "yellow", "green", "blue", "purple"]
odds = a[::2]
evens = a[1::2]
print odds
print evens

x = "mongoose"	# 翻转字符串，对字符串和ASCII字符有用，
y = x[::-1]
print y

w = u"谢谢"		# 但对于已经编码成UTF-8字符串的Unicode字符无效
x = w.encode("utf-8")
y = x[::-1]
# z = y.decode("utf-8")	# UnicodeDecodeError

a = ["a", "b", "c", "d", "e", "f", "g", "h"]	# 拆解为两条赋值语句，一条范围切割，一条步进操作
b = a[::2]
c = b[1:-1]
print c

#--------------------------------------
# 第7条：用列表推到来取代map和filter（更清晰，无需编写lambda表达式）

a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print squares
squares = map(lambda x: x**2, a)

even_squares = [x**2 for x in a if x % 2 == 0]
print even_squares
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

# dict和set也有列表类似的推到机制

chile_ranks = {"ghost": 1, "habanero": 2, "cayenne": 3}
rank_dict = {rank: name for name, rank in chile_ranks.iteritems()}
print rank_dict
chile_len_set = {len(name) for name in rank_dict.itervalues()}
print chile_len_set
# {1: 'ghost', 2: 'habanero', 3: 'cayenne'}
# set([8, 5, 7])

#--------------------------------------
# 第8条：不要使用含有两个以上表达式的列表推导
# 可以使用两个条件、两个循环、或一个条件搭配一个循环

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]			# 多重循环的用法
print flat
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [[x**2 for x in row] for row in matrix]	# 多重循环的用法
print squared

a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print b
assert b == c

matrix = [[1,2,3],[4,5,6],[7,8,9]]
filtered = [[x for x in row if x % 3 == 0]			# 晦涩难懂
			for row in matrix if sum(row) >= 10]
print filtered

#--------------------------------------
# 第9条：用生成器表达式来改写数据量较大的列表推导

value = [len(x) for x in open("hello.txt")]
print value

it = (len(x) for x in open("hello.txt"))	# 返回一个生成器
print it
print next(it)	# 获取下一个值，不用担心内存激增
print next(it)

# 生成器表达式可以相互组合
# 外围的迭代器每次前进时，会推动内部的迭代器，产生连锁效应
# 使得执行循环、评估条件表达式、对接输入和输出等逻辑都组合在了一起

roots = ((x, x**0.5) for x in it)
print next(roots)

#--------------------------------------
# 第10条：尽量用enumerate取代range
# enumerate将各种迭代器包装为生成器，以便稍后产生输出值

fruit_list = ["apple", "banana", "orange"]

# for i in range(len(fruit_list)):
# 	print "%d: %s" % (i+1, fruit_list[i])

for i, fruit in enumerate(fruit_list):	# 简洁、清爽
	print "%d: %s" % (i+1, fruit)

#--------------------------------------
# 第11条：用zip函数同时遍历两个迭代器

# 例子，获取列表中最长字符串
names = ["Lebron", "Bryant", "Wade", "HongfeiXu"]
letters = [len(n) for n in names]

longest_name = None
max_letters = 0
for i in range(len(names)):		# 同时遍历两个列表看起来很混乱
	count = letters[i]
	if count > max_letters:
		longest_name = names[i]
		max_letters = count
print longest_name

longest_name = None
max_letters = 0
for name, count in zip(names, letters):	# 清爽很多
	if count > max_letters:
		longest_name = name
		max_letters = count
print longest_name

# 注1：Python2中zip并不是生成器，会将提供的迭代器全部平行的遍历一次，将完整的远足列表返回给调用者，可能会带来内存剧增
# 如果要遍历数据量较大的迭代器，应该使用itertools内置模块中的izip，见第46条

# 注2：如果输入的迭代器长度不同，则当一个耗尽，zip就不再产生元组了
# 如果不能确定zip所封装的列表是否等长，则可考虑使用itertools中的zip_longest函数，Python2中叫做izip_longest

#--------------------------------------
# 第12条：不要在for和while循环后面写else块

a = 4
b = 9
for i in range(2, min(a, b) + 1):
	print "Testing %d" % i
	if a % 2 == 0 and b % i == 0:
		print "Not coprime"
		break
else:
	print "Coprime"

def coprime(a, b):
	for i in range(2, min(a, b) + 1):
		if a % 2 == 0 and b % i == 0:
			return False
	return True

#--------------------------------------
# 第13条：合理利用try/except/else/finally结构中的每个代码块

# 1. finally块
# 既要将异常向上传播，又要在异常发生时执行清理工作，则使用try/finally结构
# 常见用途，确保程序能够可靠地关闭文件句柄

handle = open("hello.txt")	# May raise IOError
try:
	data = handle.read()	# May rasie UnicodeDecodeError
finally:
	handle.close()			# Always runs after try:

# 2. else块
# try/except/else结构可以清晰地描述出哪些异常会由自己的代码来处理、哪些异常会传播到上一级
# 如果try没有发生异常，那么就执行else块
# else块可以尽量缩减try块内的代码量

import json
def load_json_key(data, key):
	try:
		result_dict = json.loads(data)	# May raise ValueError
	except ValueError as e:	# 捕获处理 ValueError
		raise KeyError(e)
	else:
		return result_dict[key]			# May raise KeyError，若有异常，则向上传播

# 3. 混合使用

UNDEFINE = object()

def divide_json(path):
	handle = open(path, "r+")		# May raise IOError
	try:
		data = handle.read()		# May raise UnicodeDecodeError
		op = json.loads(data)		# May raise ValueError
		value = (
			op["numerator"]/
			op["denominator"])		# May raise ZeroDivisionError
	except ZeroDivisionError as e:
		return UNDEFINE
	else:
		op["result"] = value
		result = json.dumps(op)
		handle.seek(0)
		handle.write(result)		# May raise IOError
		return value
	finally:
		handle.close()				# Always runs










