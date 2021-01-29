# -*- coding: utf-8 -*-

# 第三章 类与继承

# 注：善用类和继承，可以写出易于维护的代码。

#--------------------------------------
# 第22条：尽量用辅助类来维护程序的状态，而不要用字典和元组

# 把嵌套结构重构为类
# 元组的元素一旦超过两个就考虑用别的方法来实现了

# 要点：
# 1. 不要使用包含其他字典的字典，也不要使用过长的元组
# 2. 如果容器中包含简单又不可变的数据，可以先使用namedtuple来表示，待稍后有需要，再修改为完整的类
# 3. 保存内部状态的字典如果变得比较复杂，就应该将其拆分为多个辅助类


# 例子：存学生的成绩

import collections
"""
成绩，权重
"""
Grade = collections.namedtuple("Grade", ("score", "weight"))


class Subject(object):
	"""
	科目，包含一系列考试成绩
	"""
	def __init__(self):
		self._grades = []

	def report_grade(self, score, weight):
		self._grades.append(Grade(score, weight))

	def average_grade(self):
		total, total_weight = 0, 0
		for grade in self._grades:
			total += grade.score * grade.weight
			total_weight += grade.weight
		return total / total_weight


class Student(object):
	"""
	学生，包含此学生正在学习的各项课程，以课程名为键
	"""
	def __init__(self):
		self._subjects = {}

	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()
		return self._subjects[name]

	def average_grade(self):
		total, count = 0, 0
		for subject in self._subjects.values():
			total += subject.average_grade()
			count += 1
		return total / count


class GradeBook(object):
	"""
	成绩，包含所有学生考试成绩的容器类，以学生名字为键
	"""
	def __init__(self):
		self._students = {}

	def student(self, name):
		if name not in self._students:
			self._students[name] = Student()
		return self._students[name]

book = GradeBook()
albert = book.student("Albert Einstein")
math = albert.subject("Math")
math.report_grade(80, 0.10)
print(albert.average_grade())
print(book.student("Albert Einstein").average_grade())

#--------------------------------------
# 第23条：简单的接口应该接受函数，而不是类的实例

# Python有许多内置API，允许调用者传入函数，以定制其行为。
# API执行的时候，会通过这些挂钩(hook)函数，回调函数内部的代码。
# 如list类型的sort方法接受可选的key参数，用以指定每个索引位置上的值之间应该如何排序。

# Python中函数之所以能充当挂钩，原因在于，它是一级对象，可以像语言中其他值那样传递和引用

names = ["Lebron", "Micheal", "Kobe", "Davis"]
names.sort(key=lambda x : len(x))

d = {"Lebron": 2, "Jordan": 1, "Kobe": 3}
print(sorted(d.items(), key = lambda item: item[1]))

# 需求1：在字典中找不到待查询的键时打印一条信息，并返回0，作为该键对应的值。

def log_missing():
	print("Key added")
	return 0

current = {"green": 12, "blue": 3}
increments = [
	("red", 5),
	("blue", 17),
	("orange", 9),
]
result = collections.defaultdict(log_missing, current)
print("Before:", dict(result))
for key, amount in increments:
	result[key]	 += amount
print("After:", dict(result))

# 需求2：统计出该字典一共遇到了多少个缺失的键，一种实现方式是使用带状态的闭包

def increment_with_report(current, increments):
	added_count = 0

	def missing():
		nonlocal added_count	# stateful closure
		added_count += 1
		return 0

	result = collections.defaultdict(missing, current)
	for key, amount in increments:
		result[key] += amount
	return result, added_count

# 尽管defaultdict并不知道missing挂钩函数中保存了状态，但运行上面的函数可以产生预期的结果
# 这就是令接口接受简单函数的好处，把状态隐藏到闭包里，稍后我们就可以方便地为闭包函数添加新的功能

current = {"green": 12, "blue": 3}
increments = [
	("red", 5),
	("blue", 17),
	("orange", 9),
]
result, added_count = increment_with_report(current, increments)
print("result = {}, added_count = {}".format(dict(result), added_count))

# 另一种实现方式是使用一个小型的类，相较于带状态的闭包函数，会有较好的可读性

class CountMissing(object):
	def __init__(self):
		self.added = 0

	def missing(self):
		self.added += 1
		return 0

counter = CountMissing()
current = {"green": 12, "blue": 3}
increments = [
	("red", 5),
	("blue", 17),
	("orange", 9),
]
result = collections.defaultdict(counter.missing, current)
for key, amount in increments:
	result[key] += amount

print("result = {}, counter.added = {}".format(dict(result), counter.added))

# 继续优化，定义__call__特殊方法，使得相关对象能像函数一样被调用

class BetterCountMissing(object):
	def __init__(self):
		self.added = 0

	def __call__(self):	# __call__方法强烈地暗示这个类的用途，告诉我们这个类就相当于一个带有状态的闭包
		self.added += 1
		return 0

counter = BetterCountMissing()
current = {"green": 12, "blue": 3}
increments = [
	("red", 5),
	("blue", 17),
	("orange", 9),
]
result = collections.defaultdict(counter, current)	# Relies on __call__，比上面的counter.missing清晰很多
for key, amount in increments:
	result[key] += amount

print("result = {}, counter.added = {}".format(dict(result), counter.added))





