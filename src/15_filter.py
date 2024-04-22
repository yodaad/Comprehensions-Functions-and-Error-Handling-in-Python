"""Filter function is used to filter the elements of a sequence based on a condition. It takes a function and a sequence as arguments and returns a new sequence with 
the elements that satisfy the condition."""

numbers = [1, 2, 3, 4, 5, 6]

# Filter the numbers that are even from the list of numbers and store them in a new list called new_numbers using the filter function. 
new_numbers = list(filter(lambda x: x %  2 == 0, numbers))
print(new_numbers)
print(numbers)