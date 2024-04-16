"""Scope: The region of the program where a variable is recognized. Parameters and variables defined inside a function are not visible from outside the function. 
Hence, they have a local scope. A variable declared outside a function has a global scope. Global variables can be used by functions within the program."""

# Example 1 - Global variable
price = 100

# Function to increment the price
def increment():
    
    # Local variable price inside the function increment 
    price = 200
    result = price + 10
    print("Result: ",result)
    return result

# Call the function
print(price)
price_2 = increment()