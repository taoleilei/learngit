class Mapper:
    """docstring for Mapper"""
    __mapper_relation = {}

    @staticmethod
    def register(cls, value):
        Mapper.__mapper_relation[cls] = valueo

    @staticmethod
    def exist(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False

    @staticmethod
    def value(cls):
        return Mapper.__mapper_relation[cls]


class MyType(type):
    """docstring for MyType"""
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        # print(cls) ==> cls是Foo
        # print('============')
        arg_list = list(args)
        if Mapper.exist(cls):
            value = Mapper.value(cls)
            arg_list.append(value)
        obj.__init__(*arg_list, **kwargs)
        return obj


class Foo(metaclass=MyType):
    """docstring for Foo"""

    def __init__(self, arg):
        print('++++++++++')
        self.arg = arg

    def f1(self):
        return self.arg.upper()


class Bar(metaclass=MyType):
    """docstring for Foo"""

    def __init__(self, arg):
        print('----------')
        self.arg = arg

    def f1(self):
        return self.arg


Mapper.register(Foo, '666')
Mapper.register(Bar, '999')
obj = Foo()
# obj = Bar()
# print(obj)
print(obj.f1())
