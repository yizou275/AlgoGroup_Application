import random
from option1 import find_duplicate_one, find_duplicate_two

#tests on Method 1
#tests on empty lists
def test_method1_0():
    assert find_duplicate_one([]) == -1

#tests on valid "input" lists
def test_method1_1():
    assert find_duplicate_one([1, 2, 1]) == 1

def test_method1_2():
    assert find_duplicate_one([3, 1, 2, 3]) == 3

def test_method1_3():
    assert find_duplicate_one([4, 2, 1, 2, 3]) == 2

def test_method1_4():
    new_input: list[int] = []
    for i in range(100):
        new_input.append(i+1)
    r: int = random.randrange(1, 100)
    new_input.append(r)
    assert find_duplicate_one(new_input) == r

#tests on invalid "input" lists
def test_method1_5():
    assert find_duplicate_one([1]) == -1

def test_method1_6():
    assert find_duplicate_one([3, 4, 1, 2]) == -1

def test_method1_7():
    assert find_duplicate_one([1, 1, 1, 2]) == -1

def test_method1_8():
    assert find_duplicate_one([1, -2, 1, 2]) == -1

def test_method1_9():
    assert find_duplicate_one([2, 10, 1, 2]) == -1


#tests on Method 2
#tests on empty lists
def test_method2_0():
    assert find_duplicate_two([]) == -1

#tests on valid "input" lists
def test_method2_1():
    assert find_duplicate_two([1, 2, 1]) == 1

def test_method2_2():
    assert find_duplicate_two([3, 1, 2, 3]) == 3

def test_method2_3():
    assert find_duplicate_two([4, 2, 1, 2, 3]) == 2

def test_method2_4():
    new_input: list[int] = []
    for i in range(100):
        new_input.append(i+1)
    r: int = random.randrange(1, 100)
    new_input.append(r)
    assert find_duplicate_two(new_input) == r

#tests on invalid "input" lists
def test_method2_5():
    assert find_duplicate_two([1]) == -1

def test_method2_6():
    assert find_duplicate_two([3, 4, 1, 2]) == -1

def test_method2_7():
    assert find_duplicate_two([1, 1, 1, 2]) == -1

def test_method2_8():
    assert find_duplicate_two([1, -2, 1, 2]) == -1

def test_method2_9():
    assert find_duplicate_two([2, 10, 1, 2]) == -1
