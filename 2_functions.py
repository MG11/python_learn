a = 10
class functions():
    def greet(self):
        # check for return type
        print("test")
        print("test2")
        return 'a', 'b' # returns tuple
    
    # none of pass by value or reference, 
    def update(self, x):
        print('id x', id(x))
        x = 8
        print("x ", x) #8
        print('id x', id(x)) # the moment we change value, it changes id,
        # creates new address as integers, strings are immutable

    #formal arguments: a, b
    def add1(self, name, age):
        pass

    #default arguments is age here
    def test(self, name, age=10):
        pass

    #variable length arguments #args
    def sum(self, a, *b):
        c = a # takes 5
        # *b takes 6,7,8,9 as tuple needs for loop
        print(a)
        for i in b:
            c += i
        print(c)
    
    #kwargs
    def person(self, name, **data):
        print(data) #dict
        print(name) # navin
        pass

    def global_local(self):
        global a
        a = 20

        #another way without declaring a global variable
        #globals()['a']
        globals()['a'] = 15

    def lambda_fns(self):
        # you can pass functions as well in functions
        # anonymous functions
        # functions are objects
        # a : a*a #left side is value passed, right passed is value returned
        f = lambda a : a*a
        print(f(5))

        # there should be only one expression
        f2 = lambda a, b: a+b
        print(f2(4,7))

    def lamba_use(self):
        nums = [1,2,3,4,5,6]
        # lambda function
        # filter values
        evens = list(filter(lambda a: a%2 == 0, nums))
        print(evens)

        # double values
        double = list(map(lambda a: a*2,evens))
        print(double)

        # reduce values
        

import  sys
sys.setrecursionlimit(10)

d = functions()

d.lamba_use()
d.lambda_fns()
print(a)
d.global_local()
print(a) # changed due to fn global local

#variable length
d.sum(5,6,7,8,9)

# keyward variable length arguments
d.person('navin', age=28, city='mumbai', mob='12344')

print(d.add1(5,4))
print(d.greet())

a = 10
print('id a', id(a))
d.update(a)
print("a ", a) # 10, did not update for immutate but update for mutuable like lists

#actual arguments
d.add1('megha',6)

#keyword arguments, we dont have to care about position
d.add1(age=20, name='megha')

# while calling fn having default arguments, you can skip default argumment
d.test('megha')
d.test('megha', 40)
