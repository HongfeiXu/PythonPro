#coding=utf-8

# refs: https://refactoringguru.cn/design-patterns/builder
# refs: https://refactoringguru.cn/design-patterns/builder/python/example

# 生成器模式
# 亦称：建造者模式，Builder
# 生成器模式是一种创建型设计模式， 使你能够分步骤创建复杂对象。
# 该模式允许你使用相同的创建代码生成不同类型和形式的对象。

# 生成器模式建议将对象构造代码从产品类中抽取出来， 并将其放在一个名为生成器的独立对象中。
# 生成器模式让你能够分步骤创建复杂对象。 生成器不允许其他对象访问正在创建中的产品。

# 生成器重点关注如何分步生成复杂对象。 抽象工厂专门用于生产一系列相关对象。
# 抽象工厂会马上返回产品， 生成器则允许你在获取产品前执行一些额外构造步骤。

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
	"""
	The Builder interface specifies for creating the different parts of
	the Product objects.
	"""

	@property
	@abstractmethod
	def product(self) -> None:
		pass

	@abstractmethod
	def produce_part_a(self) -> None:
		pass

	@abstractmethod
	def produce_part_b(self) -> None:
		pass

	@abstractmethod
	def produce_part_c(self) -> None:
		pass

class ConcreteBuilder(Builder):
	"""
	The Concrete Builder classes follow the Builder interface and provide
	specific implementations of the building steps. Your program may have
	several variations of Builders, implemented differently.
	"""

	def __init__(self) -> None:
		"""
		A fresh builder instance should contain a blank product object, which is
        used in further assembly.
		"""
		self.reset()

	def reset(self) -> None:
		self._product = Product1()

	@property
	def product(self) -> Product1:
		"""
		Concrete Builders are supposed to provide their own methods for
		retrieving results. That's because various types of builders may create
		entirely different products that don't follow the same interface.
		Therefore, such methods cannot be declared in the base Builder interface
		(at least in a statically typed programming language).

		Usually, after returning the end result to the client, a builder
		instance is expected to be ready to start producing another product.
		That's why it's a usual practice to call the reset method at the end of
		the `getProduct` method body. However, this behavior is not mandatory,
		and you can make your builders wait for an explicit reset call from the
		client code before disposing of the previous result.
		"""
		product = self._product
		self.reset()
		return product

	def produce_part_a(self) -> None:
		self._product.add("PartA1")

	def produce_part_b(self) -> None:
		self._product.add("PartB1")

	def produce_part_c(self) -> None:
		self._product.add("PartC1")


class Product1(object):
	"""
	It makes sense to use the Builder pattern only when your products are quite
	complex and require extensive configuration.

	Unlike in other creational patterns, different concrete builders can produce
	unrelated products. In other words, results of various builders may not
	always follow the same interface.
	"""

	def __init__(self) -> None:
		self.parts = []

	def add(self, part: Any) -> None:
		self.parts.append(part)

	def list_parts(self) -> None:
		print(f"Product parts: {', '.join(self.parts)}", end="")


class Director(object):
	"""
	The Director is only responsible for executing the building steps in a
	particular sequence. It is helpful when producing products according to a
	specific order or configuration. Strictly speaking, the Director class is
	optional, since the client can control builders directly.
	"""
	def __init__(self) -> None:
		self._builder = None

	@property
	def builder(self) -> Builder:
		return self._builder

	@builder.setter
	def builder(self, builder: Builder) -> None:
		"""
		The Director works with any builder instance that the client code passes
		to it. This way, the client code may alter the final type of the newly
		assembled product.
		"""
		self._builder = builder

	def build_minimal_viable_product(self) -> None:
		self._builder.produce_part_a()

	def build_full_featured_product(self) -> None:
		self.builder.produce_part_a()
		self.builder.produce_part_b()
		self.builder.produce_part_c()


if __name__ == "__main__":
	"""
	The client code creates a builder object, passes it to the director and then
	initiates the construction process. The end result is retrieved from the
	builder object.
	"""

	director = Director()
	builder = ConcreteBuilder()
	director.builder = builder

	print("Standard basic product: ")
	director.build_minimal_viable_product()
	builder.product.list_parts()
	print("\n")
	director.build_full_featured_product()
	builder.product.list_parts()
	print("\n")
	print("Custom product: ")
	builder.produce_part_a()
	builder.produce_part_c()
	builder.product.list_parts()

"""
Standard basic product: 
Product parts: PartA1

Product parts: PartA1, PartB1, PartC1

Custom product: 
Product parts: PartA1, PartC1
"""