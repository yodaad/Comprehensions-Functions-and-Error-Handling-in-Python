"""
Return statement in Python is used to return a value from a function. The return statement is followed by an expression which is evaluated. 
The value of the expression is returned to the caller as the “fruit” of calling the function. The return statement can be used to return multiple values from a function.
"""

# Example 1 - Create a function that returns a value adding two numbers and returns the result of the sum of the two numbers.
def sum_with_range (min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

# Call the function with arguments
result = sum_with_range(1, 10)
print(result)

# Example 2 - Create a function that returns a value adding two numbers and returns the result of the sum of the two numbers.
result_2 = sum_with_range(result, result + 10)
print(result_2)

