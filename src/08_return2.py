# Return multiple values from a function using a tuple or a list in Python.  

# Example 1 - Return a tuple from a function with default values
def find_volume (length = 1, width = 1, depth = 1):
    return length * width * depth, width, "Hello"

# Call the function and unpack the tuple into variables 
result, width, text = find_volume(width = 10)
print(result)
print(width)
print(text)