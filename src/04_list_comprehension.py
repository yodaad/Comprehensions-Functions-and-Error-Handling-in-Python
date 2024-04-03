# List comprehension is a concise way to create lists. It is a way to create lists using a single line of code. It is a more concise way to create lists than using a for loop


# Example 1 - Create a list of numbers from 1 to 10 using a for loop
numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print("Numbers: ", numbers)

# List comprehension syntax - [expression for element in iterable]
numbers_2 = [element * 2 for element in range (1, 11)]
print("Numbers 2: ",numbers_2)


# Example 2 - Create a list of numbers from 1 to 10 that are even using a for loop
numbers_3 = []

for i in range(1, 11):
    if i % 2 == 0:
        numbers_3.append(i * 2)
    
print("Numbers 3: ",numbers_3)

# List comprehension syntax - [expression for element in iterable if condition]
numbers_4 = [i * 2 for i in range (1, 11) if i % 2 == 0]
print("Numbers 4: ",numbers_4)