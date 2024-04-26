"""Iterable is an object that can be iterated over. It returns an iterator when iter() function is called on it. It can be a list, tuple, set, dictionary, string, etc. 
It can be iterated over using for loop or next() function. It gets exhausted after one full iteration."""

# Example 1: Iterating over a list using for loop
for i in range (1, 11):
    print(i)

# Example 2: Iterating over a list using iter() function
my_iterable = iter(range(1, 11))

# Print the iterable object
print(my_iterable)

# Print the iterable object using next() function
print("First iterable with next function: ",next(my_iterable))
print("Second iterable with next function: ",next(my_iterable))

# Print the iterable object using for loop
for number in my_iterable:
    print("Remaining iterables: ",number)

"""
This will raise an error as the iterable object has already been iterated over in the above for loop and the iterator is exhausted. 
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
"""
