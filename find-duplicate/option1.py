# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer

def find_duplicate_one(input: List[int]) -> int:
    '''
    Method 1. I start putting items in "input" to a set and stop when a duplication occurs, which is 
    when the item is already in the set.
    This method takes up more space, as a set needs to be stored, but it's faster since we don't
    need to reach the end of the "input" list to find the duplicate value (haven't learned about
    complexity, but should be at most O(n)?).
    '''
    #check pre-conditions
    if not valid_input(input):
        return -1 #for testing/debugging purpose, could also raise an Exception (forgot how Exceptions are tested)

    covered_numbers: set = set()
    for i in input:
        if i in covered_numbers:
            return i
        covered_numbers.add(i)

    return 0
    #this final line won't be reached, but is kept for compiling and debugging purposes


def find_duplicate_two(input: List[int]) -> int:
    '''
    Method 2. Since the "input" list has N+1 entries and must cover values from 1 to N, this method
    removes each value from 1 to N from the list. Since the "remove" method in list will only remove
    the first one if the value is duplicated, the list will only remain the duplicate value after 
    such deletion, which is the returned value.
    This method saves space and doesn't require anything more to store, but it will take more time
    since all the values from 1 to N must be removed to find the duplicate value (should be exactly
    O(n)?).
    '''
    #check pre-conditions
    if not valid_input(input):
        return -1 #same as Method 1, could also raise an Exception

    length: int = len(input)

    for i in range(length - 1): #if pre-condition met, length - 1 > 0
        input.remove(i+1) # if pre-condition met, i+1 must be in "input"
    return input[0]


def valid_input(input: List[int]) -> bool:
    '''
    A helper method that checks the "input" list matches the pre-condition.
    '''
    length: int = len(input)

    input_set: set = set(input)
    if not len(input_set) == length - 1:
        return False
    for i in range(length - 1):
        if i+1 not in input_set:
            return False

    return True
