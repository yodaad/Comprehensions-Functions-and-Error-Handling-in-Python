"""Reduce function is used to apply a function to all of the elements in an iterable and reduce them to a single value. It takes a function and an iterable as arguments and returns 
a single value. The function is applied cumulatively to the elements of the iterable. The reduce function is available in the functools module in Python 3.0 and above.""" 

import functools

numbers = [1, 2, 3, 4]

# Example 1: Calculate the sum of all the numbers in the list using the reduce function.
result = functools.reduce(lambda i, item: i + item, numbers)
print(result)

# Example 2: Calculate the difference of all the numbers in the list using the reduce function with a custom function.
def accum(i, item):
    print("counter => ", i)
    print("item => ", item)
    return i - item

result2 = functools.reduce(accum, numbers)
print(result2)
