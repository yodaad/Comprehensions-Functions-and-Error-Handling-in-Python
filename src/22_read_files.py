"""Read files in Python - Python provides a built-in function open() to open a file. The open() function returns a file object, which has a read() method 
for reading the content of the file."""

# Open a file in read mode - "r" is the default mode
file = open("./text.txt")

""" 
Reads libe by line of a file.

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""
# print(file.read()) Reads all lines at the same time

# Read the file line by line using a for loop and print each line to the console 
for line in file:
    print(line)

file.close()

"""Most common syntaxis to read a file in Python is using the with statement to ensure that the file is properly closed after its suite finishes, even if an exception is 
raised during the process. file.close() is not necessary because the with statement automatically closes the file when the block of code is executed."""
with open("./text.txt") as file:
    for line in file:
        print(line)
