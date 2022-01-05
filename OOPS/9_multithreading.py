# breaking big task to small tasks
 # breaking big task to small parts and breaking those parts in thread

 # every application has multiple threads
 # they can run on multiple cores simultaneously
# multitasking

# by default there is one thread only
# threads can be used to execute fns / applications simultaneously

from threading import *
from time import *
class Hello(Thread):

    def run(self):
        for i in range(5):
            #  add sleep so that scheduler dont add them all in one go and Hi can be printed
            sleep(1)
            print('Hello')

class Hi(Thread):

    def run(self):
        for i in range(5):
            sleep(1)
            print('Hi')


t1 = Hello()
t2 = Hi()

# start is fun in thread used to start thread
t1.start()
# to avoid colloision so that both dont start at same time
sleep(0.2)
t2.start()

# t1, t2 finish their executions
t1.join()
t2.join()

# this is build by main thread
print("bye")