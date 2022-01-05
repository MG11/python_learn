"""
duck typing
operator overloading
method overloading
method overriding
"""
# duck typing
x = 5 
x = 'Navin' #adress of x changes

class ducktyping:
    class Pycharm:
        def execute(self):
            print("in pycharm")

    class MyEditor:
        def execute(self):
            print("in my editor")
    
    class Laptop:
        def code(self, ide):
            # duck typing means we dont care about type 
            # of ide, it just should have method execute
            ide.execute()

    def __init__(self):
        lap = self.Laptop()
        lap.code(self.MyEditor())
        lap.code(self.Pycharm())

# ducktyping()

class operator_overloading:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        # print(int.__add__(a,b))

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return operator_overloading(m1, m2)
    
    def __gt__(self, other):
        # compare two objects
        pass
        
    def __str__(self) -> str:
        return '{} {}'.format(self.m1, self.m2)
    
    @staticmethod
    def start():
        s1 = operator_overloading(12,13)
        s2 = operator_overloading(15, 16)
        print(s1)
        # s1.__str__ is called behind the scenes
        s3 = s1 + s2  #operator_overloading.__add__(s1, s2) + means call __add__ method

# operator_overloading.start()


class method_overloading:

    def __init__(self) -> None:
        # not supported directly in python.
        # method overloading means, two functions with same name and different parameters.
        pass

    # we do method overloading by using default arguments
    def sum(a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a+b+c
        elif a!=None and b != None:
            return a+b
        else:
            return c

class method_overriding:

    def show(self):
        print("in A show")
    
# B overrides show of method_overriding  if B does not has its show function
# if we have show in child class, it will use that only
class B(method_overriding):
    pass

a1 = B()
a1.show()
