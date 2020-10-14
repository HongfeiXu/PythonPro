#coding=utf-8

# refs: https://refactoringguru.cn/design-patterns/factory-method
# refs: https://refactoringguru.cn/design-patterns/factory-method/python/example

# 工厂方法模式
# 亦称： 虚拟构造函数、 Virtual Constructor、 Factory Method

# 工厂方法是一种创建型设计模式， 解决了在不指定具体类的情况下创建产品对象的问题。
# 工厂方法定义了一个方法， 且必须使用该方法代替通过直接调用构造函数来创建对象 （ new 操作符） 的方式。
# 子类可重写该方法来更改将被创建的对象所属类。


from __future__ import annotations
from abc import ABC, abstractmethod


# 创建者类声明的工厂方法必须返回一个产品类的对象。创建者的子类通常会提供
# 该方法的实现。
class Creator(ABC):
	"""
	请注意，创建者的主要职责并非是创建产品。其中通常会包含一些核心业务
	逻辑，这些逻辑依赖于由工厂方法返回的产品对象。子类可通过重写工厂方
	法并使其返回不同类型的产品来间接修改业务逻辑。
	"""
	@abstractmethod
	def factory_method(self):
		pass

	def some_operation(self) -> str:
		product = self.factory_method()
		result = f"Creator: The same creator's code has just worked with {product.operation()}"
		return result


# 具体创建者将重写工厂方法以改变其所返回的产品类型。
class ConcreteCreator1(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct1()


class ConcreteCreator2(Creator):
	def factory_method(self) -> Product:
		return ConcreteProduct2()


# 产品接口中将声明所有具体产品都必须实现的操作。
class Product(ABC):
	@abstractmethod
	def operation(self) -> str:
		pass


class ConcreteProduct1(Product):
	def operation(self) -> str:
		return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
	def operation(self) -> str:
		return "Result of the ConcreteProduct2"


def client_code(creator: Creator) -> None:
	print(f"Client: I'm not aware of the creator's class, but it still works.\n"
		  f"{creator.some_operation()}", end="")

if __name__ == "__main__":
	print("App: Launched with the ConcreteCreator1.")
	client_code(ConcreteCreator1())
	print("\n")

	print("App: Launched with the ConcreteCreator2.")
	client_code(ConcreteCreator2())