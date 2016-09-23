import abc


class Foo(metaclass=abc.ABCMeta):
    """docstring for Foo"""
    def f1(self):
        print('123')

    def f2(self):
        print('456')

    @abc.abstractmethod
    def f3(self):
        """
        """

class Bar(Foo):
    """docstring for Bar"""
    def f1(self):
        print('666')
    def f3(self):
        print('999')

b = Bar()
b.f1()
b.f3()