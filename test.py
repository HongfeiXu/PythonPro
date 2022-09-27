class Foo(object):
    def __init__(self):
        self.num = 0

def test():
    a = Foo()
    b = Foo()
    s = set()
    s.add(a)
    s.add(b)
    print(s)

test()