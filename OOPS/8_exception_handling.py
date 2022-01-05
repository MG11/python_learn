"""
compiler time : example forgot to add colon
logical : response is wrong
runtime error: divide by 0
syntax error
"""

a = 5
b = 0
try:
    print("resourse open")
    print(a/b) # critical statement, put them in try, run time error
except ZeroDivisionError as ex:
    print("Hey, u cannot divide by zero")
except ValueError as ex:
    print("invalid input")
except Exception as e:
    print("something went wrong!!")

finally:
    # it executes every time in case of exception or not..
    print("resource closed")

print("bye")

