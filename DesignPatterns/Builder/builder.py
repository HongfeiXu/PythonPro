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




