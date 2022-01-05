
class structures():
    def strings(self):
        print('navin\'s  "laptop"') # \ after ' means to ignore ' 
        print(r'navin \nnavin') # r means to consider it as raw string
        #  strings in python are immutable

    def lists(self):
        # list are mutuable
        nums = ["abc", 12]
        nums2 = ["def", 13]
        mil = [nums, nums2]
        print(mil)  #[['abc', 12], ['def', 13]]

        nums.insert(0, "megha")
        print(mil) #[['megha', 'abc', 12], ['def', 13]]
        nums.clear()
        print(mil) #[[], ['def', 13]]
        nums2.insert(4, "me")
        print(mil)  #[[], ['def', 13, 'me']]
        nums2.pop(1) 
        print(mil) #[[], ['def', 'me']]
        nums2.pop()
        print(mil) #[[], ['def']]

        del mil [1:]
        print(mil) #[[]]

        mil.extend([12,13,14,15]) 
        print(mil)  #[[], 12, 13, 14, 15]

        # print(min(mil))  gives error as mil has list
        # print(max(mil))

    def tuples(self):
        # tuple
        tup = (21, 36,14,25)
        # tuple are immutable
        print(tup)
    
    def sets(self):
         # values should be of immutable type 
        s = {21, 23, 14, 4,64}
        print(s)
        s.pop()
        #s.remove(2) #gives error
        s.discard(2) # does not give error
        print(s)
        s.remove(21)
        print(s)
        s = {(1,2,3), (2,3,4), (1,2,3), 'megha'}
        print(s)

        # set stores unique values does not maintain order
        # indexing is not supported

    def dictionaries(self):
        data = dict()
        # key should be immutable, should be unique
        data = {'1': 'anb', '2': 3, '33': 45}
        print(data['1'])
        # data.clear()
        data.get(20)  # will not give error
        keys = ['Navin', 'Kiran', 'Harsh']
        values = ['Python', 'Java', 'JS']
        print(zip(keys, values))
        data = dict(zip(keys, values))
        print(data)
        # delete values 
        del data['Harsh']
        print(data)
        prog = {'JS': 'Atom', 'CS': 'VS',
         'Python': ['Pycharm', 'Sublime'], 'Java': 
             {'JSE': 'Netbeans', 'JEE': 'Eclipse'}
         }
        print(prog['Java']['JSE'])

    def variables(self):
        num = 5
        print(id(num))
        a = num
        print(id(a)) # id of a and num will be same
        #both will point to same address
        num = 6
        print(id(num)) #now, id of num is changed
        # memory locations are garbage collected when it is not tagged

        PI = 3.14 # to show it is constant
        # in python we dont have const thing 

    def dataTypes(self):
        # None
        # numeric : int, float, complex, bool
        num = 2
        num = 2.5
        num = 1 + 2j
        num = True
        b = int(5.6)
        print(b) #5
        b = float(5)
        print(b) #5.0
        # sequence: list, tuple, set, string, range
        # we dont have char type here 
        list(range(2)) #[0,1]

        list(range(2,10,2)) 
        # [2,4,6,8]

        # mapping: dictionary
        
    def operators(self):
        a, b = 5,6
        print(a) #5
        print(b) #6
        a = -a 
        print(a) #-5
    
    def number_system(self):
        print(bin(25))
        print(0b101) #print 3
        oct(25) #0o31
        hex(25) #0x19

        print(~12) #-13
        print( 12 & 13) #bithwise end, both sides are executed
        print(12 | 13) #bitwise or
        print(12 ^ 13) #xor
        print(10 << 2) #left shift, gaining bits
        print(10 >> 2) #right shift, loosing 2 bits

        a = 5
        b = 6
        c = 7
        # evaluates right hand side and puts it in stack and rotate
        #then left hand sides are assigned two -root

        a, b ,c = b, c, a
        print(a,b,c)

    def user_input(self):
        x = int(input("enter x: ")) # always returns string type by default, convert it in string
        y = int(input("enter y: ")) 
        print(x +y)
        result = eval(input('enter an expr'))
        print(result)
        
        # pass
        for i in range(10):
            if( i%2 != 0):
                pass  #there is no code, ignore it 
            else: print(i, end='')
    
    def conditionals(self):
        # for else
        count = 2
        while (count < 1):
            count = count+1
            print(count)
            break
        else:
            # execuates when loop is exited without executing break 
            # in the code or break statement is not there
            print("No Break") 

    def arrays(self):
        # similar to lists but of same type
        from array import array
        vals = array('i', [5,9,8,4,2])
        print(len(vals))
        vals.reverse()
        print(vals)
        newArr = array(vals.typecode, (a for a in vals))
        newArr = vals #copies address
        # newArr = vals.copy() gives error
        vals = array('i', [])
        vals.append(10)
        print(vals)
        print(newArr)
        pass
    
    def copies(self):
        arr1 = array([2,6,8,1,'rest']) #all values become string type
        arr2 = arr1 #copies address
        print(arr1.dtype)
        print(arr1)
        print(id(arr1), id(arr2))
        #shallow copy, creates new address for arr2 but
        #elements are still dependent on each other
        arr2 = arr1.view() #to create copies shallow copy
    
        #deepcopy # creates copy of element 
        arr2 = arr1.copy()


from numpy import *
# import sys
# brackets are optional in for, while and if statements
# x = sys.argv[1]
# print(x)  prints data passed from file name, argv[0] will give file path
d = structures()
d.copies()
