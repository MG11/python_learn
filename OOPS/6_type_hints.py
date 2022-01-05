# it is for documentation purpose only, if we dont define type like this our program will not crash
# use static code analysis tool

x : int = 1   # x should store string 

def add_numbers(a : int, b: int, c: int) -> int:
    return a + b + c


def add_number(a: int, b: int, c:int) -> None:
    print(a + b + c)

from typing import Callable, List, Dict, Set, Optional, Any, Sequence

x: List[List[int]] = [[1,2], [3,4]]

x: Dict[str, str] = {"a" "b"}

x: Set[float] = {1.0, 2.5}

vector = List[float]

def foo(v: vector) -> vector:
    pass

v = [1.2]
foo(v)

vectors = List[vector]

def foo1(v: vectors) -> vectors:
    pass

foo1(v)

# Optional used to show this variable is optional
def foo2(output: Optional[bool]=False):
    pass

foo2()

# output can accept any type 
def foo3(output: Any):
    pass

# which have index
def foo4(seq: Sequence[str]):
    pass

foo4(['a'])
foo4(('a'))
foo4("abcdefgh")

from typing import Tuple, Callable, TypeVar

x: tuple = (1, 2 , 3 )

x: Tuple[int, int , int, str] = (1,2,3, "hello")


# callable, used when accepting fn as parameters

def add(x: int, y: int) -> int:
    return x+y

#                       parameters  return type
def foo5(func: Callable[[int, int], int]) -> None:
    func(1,2)

foo5(add)


T = TypeVar('T')

def get_item(lst: List[T], index: int) -> T:
    return lst[index]
