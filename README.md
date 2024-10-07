I'm answering Question 1, "Find Duplicate". My answer is in "option1.py".

I implement this function in two ways, with advantages respectively in time and space.

Method 1 stores a set, constantly adds elements of "input" to a set, and returns if they check a duplicate element has already appeared in the set (time advantage -- don't need to reach the end of "input").

Method 2 checks each element from 1 to N and removes its first occurrence (only occurrence for non-duplicate values) from "input", and then returns the remaining element (space advantage -- don't need to store anything new).

I also implement a helper method "valid_input" that checks the pre-condition of the function, which will return a boolean that says whether the "input" list is valid. If "valid_input" is evaluated as False, both methods will return -1 (it's more proper to raise an Exception, but sorry I forgot how Exceptions are tested in tests, so just write -1 for simplicity in tests for now).

I attach "option1_tests.py" as the tests I write, 10 tests for each method, covering scenarios of different valid or invalid inputs. All of them are passed (pls run "pytest option1_tests.py").

Also, just curious, do trees count as a container for Question 2? I was more leaning towards answering Q2 and implementing stacks by trees at first, but not sure about whether this satisfies the requirement, so finally choose Q1:)

Thank you so much!