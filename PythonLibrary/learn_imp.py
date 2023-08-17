import imp

# https://docs.python.org/zh-cn/3/library/imp.html
# 比较老的模块，已经被弃用，不推荐使用，但项目里有用到，这里稍微看下用法

target_module_name = "my_module"
target_module_path = ["test"]

def find_and_load_module(target_module_name, target_module_path):
    loaded_module = None
    try:
        file, path, definition = imp.find_module(target_module_name, target_module_path)
        # 注：imp.load_module不只是导入模块，如果模块已经被导入，它将重新加载此模块，详见文档
        try:
            loaded_module = imp.load_module(target_module_name, file, path, definition)
        finally:
            file.close()
    except ImportError as e:
        print("Failed to import module: %s" % e)
    return loaded_module


if __name__  == "__main__":
    from test import my_module
    my_module.a = 9
    my_module.foo()
    imp.reload(my_module)   # my_module 可以走 imp.reload() 重新加载
    my_module.foo()


    # 这里会重新加载这个模块
    my_module_new = find_and_load_module("my_module", ["test"])
    my_module_new.a = 12

    # my_module_new 好像只能继续走 load_module 去重新加载
    file, path, definition = imp.find_module(target_module_name, target_module_path)
    try:
        imp.load_module(target_module_name, file, path, definition)
    finally:
        file.close()
    my_module_new.foo()


"""
hello from my_module
a = 9
hello from my_module
a = 10
"""