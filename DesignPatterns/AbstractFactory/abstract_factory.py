#coding=utf-8

# refs: https://refactoringguru.cn/design-patterns/abstract-factory

# 抽象工厂模式
# 抽象工厂模式是一种创建型设计模式， 它能创建一系列相关的对象， 而无需指定其具体类。

from __future__ import annotations
from abc import ABC, abstractmethod


# 【抽象工厂】抽象工厂接口声明了一组能返回不同抽象产品的方法。这些产品属于同一个系列
# 且在高层主题或概念上具有相关性。同系列的产品通常能相互搭配使用。系列产
# 品可有多个变体，但不同变体的产品不能搭配使用。
class AbstractFactory(ABC):
	@abstractmethod
	def create_product_a(self) -> AbstractProductA:
		pass

	@abstractmethod
	def create_product_b(self) -> AbstractProductB:
		pass


# 【具体工厂】具体工厂可生成属于同一变体的系列产品。工厂会确保其创建的产品能相互搭配
# 使用。具体工厂方法签名会返回一个抽象产品，但在方法内部则会对具体产品进
# 行实例化。
class ConcreteFactory1(AbstractFactory):
	def create_product_a(self) -> AbstractProductA:
		return ConcreteProductA1()

	def create_product_b(self) -> AbstractProductB:
		return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
	def create_product_a(self) -> AbstractProductA:
		return ConcreteProductA2()

	def create_product_b(self) -> AbstractProductB:
		return ConcreteProductB2()


# 新增一种产品变体组合非常简单
class ConcreteFactory3(AbstractFactory):
	def create_product_a(self) -> AbstractProductA:
		return ConcreteProductA1()

	def create_product_b(self) -> AbstractProductB:
		return ConcreteProductB2()


# 【抽象产品】系列产品中的特定产品必须有一个基础接口。所有产品变体都必须实现这个接口。
class AbstractProductA(ABC):
	@abstractmethod
	def useful_function_a(self) -> str:
		pass


# 【具体产品】由相应的具体工厂创建。
class ConcreteProductA1(AbstractProductA):
	def useful_function_a(self) -> str:
		return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
	def useful_function_a(self) -> str:
		return "The result of the product A2."


# 这是另一个产品的基础接口。所有产品都可以互动，但是只有相同具体变体的产
# 品之间才能够正确地进行交互。
class AbstractProductB(ABC):
	@abstractmethod
	def useful_function_b(self) -> str:
		pass

	@abstractmethod
	def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
		pass


class ConcreteProductB1(AbstractProductB):
	def useful_function_b(self) -> str:
		return "The result of the product B1."

	def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
		"""
		The variant, Product B2, is only able to work correctly with the
		variant, Product A2. Nevertheless, it accepts any instance of
		AbstractProductA as an argument.
		"""
		result = collaborator.useful_function_a()
		return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
	def useful_function_b(self) -> str:
		return "The result of the product B2."

	def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
		result = collaborator.useful_function_a()
		return f"The result of the B2 collaborating with the ({result})"


# 客户端代码仅通过抽象类型（AbstractFactory、AbstractProductA 和 AbstractProductB）使用工厂
# 和产品。这让你无需修改任何工厂或产品子类就能将其传递给客户端代码。
def client_code(factory: AbstractFactory) -> None:
	product_a = factory.create_product_a()
	product_b = factory.create_product_b()
	print(f"{product_b.useful_function_b()}")
	print(f"{product_b.another_useful_function_b(product_a)}")


if __name__ == "__main__":
	print("Client: Testing client code with the first factory type: ")
	client_code(ConcreteFactory1())
	print("\n")
	print("Client: Testing client code with the second factory type: ")
	client_code(ConcreteFactory2())
	print("\n")
	# 新增一种产品变体组合
	print("Client: Testing client code with the third factory type: ")
	client_code(ConcreteFactory3())

"""
Client: Testing client code with the first factory type: 
The result of the product B1.
The result of the B1 collaborating with the (The result of the product A1.)


Client: Testing client code with the second factory type: 
The result of the product B2.
The result of the B2 collaborating with the (The result of the product A2.)


Client: Testing client code with the third factory type: 
The result of the product B2.
The result of the B2 collaborating with the (The result of the product A1.)

Process finished with exit code 0
"""