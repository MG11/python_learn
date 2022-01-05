nums = [7,8,9,6]

it = iter(nums)

# print(it)

# print(it.__next__())
# print(it.__next__())
# print(next(it))

# iterators
class TopTen:
    def __init__(self) -> None:
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1 
            return val
        else:
            raise StopIteration

# values = TopTen()

# for i in values:
#     print(i)

# generators
# generators will give iterators

# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

# this becomes a generator function as it has yield
def gen():
    # it returns iterator, returns values in format of iterator
    yield 5
    yield 6
    yield 7
    yield 8

    i = 1
    while i <=10:
        yield i
        i += 1

values = gen()
print(id(gen()))
print(id(gen()))

# print(values.__next__())
# print(values.__next__())

for i in values:
    print(i)


