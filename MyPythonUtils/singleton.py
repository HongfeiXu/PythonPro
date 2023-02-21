class Singleton(type):
    """
    单例
    参考：https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class MyClass(object, metaclass=Singleton):
    def __init__(self):
        self.data = None


if __name__ == "__main__":
    a = MyClass()
    a.data = 3
    print(a.data)
    b = MyClass()
    print(b.data)
