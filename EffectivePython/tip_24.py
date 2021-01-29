# -*- coding: utf-8 -*-

#--------------------------------------
# 第24条：以@classmethod形式的多态去通用地构建对象
import os
from threading import Thread


class InputData(object):
	def read(self):
		return NotImplementedError


class PathInputData(InputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path, encoding="utf-8").read()


class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError


class LineCountWorker(Worker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count("\n")

	def reduce(self, other):
		self.result += other.result


def generate_inputs(data_dir):
	for name in os.listdir(data_dir):
		yield PathInputData(os.path.join(data_dir, name))

def create_worker(input_list):
	workers = []
	for input_data in input_list:
		workers.append(LineCountWorker(input_data))
	return workers

def execute(workers):
	threads = [Thread(target=w.map) for w in workers]
	for thread in threads: thread.start()
	for thread in threads: thread.join()

	first, rest = workers[0], workers[1:]
	for worker in rest:
		first.reduce(worker)
	return first.result

def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers = create_worker(inputs)
	return execute(workers)

test_dir = 'D:\\Project\\PythonPro\\EffectivePython\\tip_24_test_data'
result = mapreduce(test_dir)
print(f"There are {result} lines.")

# 上述写法的MapReduce函数不够通用，如果要编写其他的InputData或Worker子类，就得重写generate_input、create_workers和mapreduce函数以匹配之。
# 因此我们重构上面的代码。

class GenericInputData(object):
	def read(self):
		raise NotImplementedError

	@classmethod
	def generate_input(cls, config):
		raise NotImplementedError


# class PathInputData2(GenericInputData):
# 	def read(self):
# 		return open()

