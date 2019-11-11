class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_square(self):
        return self.x * self.y

    """A simple example class"""
    i = 12345

    @staticmethod
    def f():
        return 'hello world'


foo = MyClass(2, 4)
print(foo.x)
print(MyClass.f())
# print(MyClass.calc_square())

