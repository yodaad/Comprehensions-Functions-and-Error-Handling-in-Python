"""Write to a file in Python - Python provides a built-in function open() to open a file. The open() function returns a file object, which has a write() method 
for writing content to the file. r+ creates new lines and w+ rewrites the current content of the file."""

# Open a file in write mode - "w" mode will overwrite the current content of the file
with open("./text.txt", "w+") as file:
    for line in file:
        print(line)
    file.write("New line replaced with w+ and file.write\n")
    file.write("Another line replaced with w+ and file.write\n")
    file.write("Yet another line replaced with w+ and file.write\n")
    
# Open a file in read mode - "r+" mode will create new lines at the end of the file
with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("New line created with r+ and file.write\n")
    file.write("Another line created with r+ and file.write\n")
    file.write("Yet another line created with r+ and file.write\n")

