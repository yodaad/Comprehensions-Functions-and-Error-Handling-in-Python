# High Order Functions (HOF) are functions that take other functions as arguments or return functions as their results.

def increment(x):
    return x + 1

# High Order Function that takes a function as an argument and returns the result of the function plus the result of the function.
def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)
print(result)

# HOF with lambda function as argument and returns the result of the lambda function plus the result of the lambda function.
increment_2 = lambda x: x + 1
high_order_function_2 = lambda x, func: x + func(x)

result = high_order_function_2(2, increment_2)
print(result)

# Result with lambda function as argument. 
result = high_order_function_2(2, lambda x: x + 2)
print(result)

result = high_order_function_2(2, lambda x: x * 5)
print(result)