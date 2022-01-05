class computer:
    # class variable, static variable  #shared in class namespace
    type = "4 gen"

    def __init__(self): #self is the object itself
        # shared in instance namespace
        # instance variable
        self.name = 'navin'
        self.__age = 28 #age become private

    def update(self):
        self.__age = 30
    
    def get_age(self):
        # created getter for the private variable
        return self.__age
    
    def compare(self, c2):
        return self.__age == c2.age


c1 = computer()
c1.update()
c2 = computer()
# print(c2.__age) will give error as age is private
print(c1.get_age())
# c1.__i_am_private_function() # gave error as this is private function
c1.access_private() # accessed private through other method

# c1.type = "tettest" changing class variable through instance, its wrong
print(computer.type) # type is class variable
print(c1.type)
print(c2.type) # changing type for c1 did not change type for c2
computer.type = "newtype"
print(c2.type)
print(c1.type)


class methods:

    # static variable
    school = 'telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        

    def __i_am_private_function(self):
        print("in private")
    
    def access_private(self):
        return self.__i_am_private_function()

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    # accessors
    def get_m1(self):
        return self.m1
    
    # modifiers
    def set_m1(self, m1 = 30):
        self.m1 = m1
    
    # working with class variable
    @classmethod
    def get_school(cls):
        return cls.school
    
    # not concered about instance or class variables
    @staticmethod
    def info():
        print("this is a stident class .. abc module")


    
c1 = methods(1,2,3)
c1.access_private() # accessed private through other method

s1 = methods(3,4,5)
print(s1.avg())
print(c1.avg())
print(methods.get_school())
methods.info()
