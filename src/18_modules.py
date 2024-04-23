"""Modules in Python are files that contain Python code. They can define functions, classes, and variables that can be used in other Python files. 
Modules are used to organize code and make it reusable."""

# Example 1 - Importing sys module and printing the path variable in the sys module 
import sys
print(sys.path)

# Example 2 - Importing the re module and using the findall function to find all the numbers in a string
import re
text = "My phone number is 300 123 4567, and the country code is 57. My lucky number is 13."
result = re.findall("[0-9]+", text)
print(result)

# Example 3 - Importing the time module and using the time function to get the current time in seconds
import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
local_result = time.asctime(local)
print(local_result)

# Example 4 - Importing the collections module and using the Counter function to count the occurrences of elements in a list
import collections
numbers = [1, 2, 2, 2, 1, 1, 3, 4, 5, 2, 3, 1, 1, 2, 2, 4, 2, 4, 2, 1]
counter = collections.Counter(numbers)
print(counter)
 
