# Sets in Python are unordered collections of unique elements. They are used to store multiple items in a single variable. Sets are written with curly brackets.

set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, "Hello", False, 12.3}
print(set_types)

# Set casting from string, tuple, list
set_from_string = set("Hello")
print(set_from_string)

set_from_tuples = set(("abc", "def", "hij", "abc"))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers2 = set(numbers)
print(set_numbers2)

unique_numbers = list(set_numbers2)
print(type(unique_numbers))
print(unique_numbers)