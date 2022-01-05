class decorators():
    pass
d = decorators()

from modules import *
# if name == __main__
print("hello", __name__) # it will print __main__ 
# but __name__ printed through other module will print modules only

def div(a, b):
    print(a/b)

def smart_div(func):
    
    def inner(a, b):
        if a < b:
            a, b = b , a
        return func(a, b)
    
    return inner

# div is passed to smart_div, which has inner function that
#  returns a new function, that new function swaps the values and calls div

div1 = smart_div(div)
div1(2,4) #here calling inner indirectly

def fun(f):

    def wrapper(*args, **kwargs):
        print('start')
        rv = f(*args, **kwargs)
        print('end')
        return rv
    
    return wrapper

def func1(x = 3):
    print("in func1 ", x)

# calling func1 directly
func1(2)

# calling through fun which returns wrapper which when called executes func1 inside
func1 = fun(func1)
func1(5)
func1()

# short way of doing this:

@fun
def func2(y, x=40):
    print("i used decorator", x, y)
    return "xyz"

print(func2(25))
