class A:
    def __init__(self) -> None:
        print("in A init")

    def feature1(self):
        print("feature 1 working")
    
    def feature2(self):
        print("feature 2 working")


# signle inheritence
class B(A): # B is child, A is parent

    def __init__(self) -> None:
        print("in B init")
        super().__init__()
        
    
    def feature3(self):
        print("feature 1 working")
    
    def feature4(self):
        print("feature 2 working")

# multilevel inheritence
class C(B):
    def feature5(self):
        print("feature 5")


class E:
    def __init__(self):
        print("in E init")

# multilevel inheritence
class D(B, E):
    def __init__(self):
        print("in D init")
        # MRO (method resolution order)
        # you need to call init explicitly
        super().__init__() # if not provided we 
        # prefer left even from function inheritence
        # to call E class init 
        E.__init__(self)
        

    def fetaure6(self):
        print("feature 6")

e = D()
