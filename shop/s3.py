# funcdict = {
#     'Foo': 'Foo 123',
#     'Bar': 'Bar 456',
#     }

class MyType(type):
    """docstring for MyType"""
    def __call__(cls, *arg, **kwarg):
        obj = cls.__new__(cls, *arg, **kwarg)
        # print(cls) ==> cls是Foo类
        # print('============')

        if isinstance(obj, Foo):
            obj.__init__('Foo 123')
        elif isinstance(obj, Bar):
            obj.__init__('Bar 456')
        else:
            obj.__init__('anything')
        return obj


class Foo(metaclass=MyType):
    """docstring for Foo"""

    def __init__(self, arg):
        print('----------')
        self.arg = arg

    def f1(self):
        print(self.arg)


class Bar(metaclass=MyType):
    """docstring for Foo"""

    def __init__(self, arg):
        print('----------')
        self.arg = arg

    def f1(self):
        print(self.arg)


class Any(metaclass=MyType):
    """docstring for Foo"""

    def __init__(self, arg):
        print('----------')
        self.arg = arg

    def f1(self):
        print(self.arg)


# obj = Foo()
obj = Bar()
# obj = Any()
print(obj)
print(obj.arg)

"""
1、遇到class Foo，执行type的__init__方法

2、遇到Foo(),执行type的__call__方法
        执行Foo类的__new__方法
        执行Foo类的__init__方法
"""
