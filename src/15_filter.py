"""Filter function is used to filter the elements of a sequence based on a condition. It takes a function and a sequence as arguments and returns a new sequence with 
the elements that satisfy the condition."""

numbers = [1, 2, 3, 4, 5, 6]

# Exmaple 1: Filter the numbers that are even from the list of numbers and store them in a new list called new_numbers using the filter function. 
new_numbers = list(filter(lambda x: x %  2 == 0, numbers))
print(new_numbers)
print(numbers)

letters = ['a', 'B', 'c', 'D', 'E', 'f']

# Example 2: Filter the letters that are uppercase from the list of letters and store them in a new list called new_letters using the filter function.
new_letters= list(filter(lambda x: x.isupper(), letters))
print(new_letters)