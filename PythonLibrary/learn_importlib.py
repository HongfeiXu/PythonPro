import importlib.util
import os
import sys

# https://docs.python.org/zh-cn/3/library/importlib.html

# ------------------------------------------------------------------------------
# spec版 加载模块，重载模块
module_name = "my_module"
module_path = os.path.realpath("test/my_module.py")
spec = importlib.util.spec_from_file_location(module_name, module_path)
my_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = my_module
spec.loader.exec_module(my_module)
my_module.foo()
my_module.a = 99
my_module.foo()

# importlib.reload(my_module) # 报错
spec.loader.exec_module(my_module) # 看起来是实现了重载
my_module.foo()
print("\n\n")

# ------------------------------------------------------------------------------
# 简单版 加载模块，重载模块
my_module2 = importlib.import_module("test.my_module")
my_module2.foo()
my_module2.a = 100
my_module2.foo()

importlib.reload(my_module2)
my_module2.foo()


"""
hello from my_module
a = 10
a = 99
hello from my_module
a = 10



hello from my_module
a = 10
a = 100
hello from my_module
a = 10

"""

