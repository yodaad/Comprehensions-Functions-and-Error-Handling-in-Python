# Error handling in Python 

# Assertions in Python - assert keyword are used to check if a condition is True. If the condition is False, the program will raise an AssertionError.
sum = lambda x, y: x + y
assert sum(2, 2) == 4

"""
This will raise an AssertionError as the sum of 2 and 2 is not equal to 5.
assert sum(2,2) == 5
"""

# Raise an exception in Python - raise keyword is used to raise an exception. It is used to raise an exception when a certain condition is not met.
age = 10
if age < 18:
    raise Exception("No underage allowed.")