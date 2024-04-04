# Dictionaries Comprehension in Python is a way to build a new dictionary by applying an expression to each item in an iterable. 

import random

# Example 1 - Create a dictionary with a for loop
dictionary = {}
for i in range (1, 5):
    dictionary[i] = i * 2

print("Dictionary: ",dictionary)


# Dictionary Comprehension Syntax - {key: value for key, value in iterable}
dictionary_2 = {i: i * 2 for i in range (1, 5)}
print("Dictionary 2: ",dictionary_2)

# Example 2 - Create a dictionary with a for loop and a condition
countries = ["col", "mex", "bol", "per"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

# Dictionary Comprehension Syntax - {key: value for key, value in iterable condition} 
population_2 = {country: random.randint(1, 100) for country in countries }
print(population_2)

names = ["Diego", "Dann", "Mike"]
ages = [39, 45, 21]

# Zip function - Combine two lists into a list of tuples
persons = list(zip(names, ages))
print(persons)

# Dictionary Comprehension with Zip function - {key: value for key, value in zip(list1, list2)}
new_dictionary = {name: age for (name, age) in zip(names, ages) }
print(new_dictionary)

# Dictionary Comprehension with Zip function and condition - {key: value for key, value in zip(list1, list2) if condition}
new_dictionary_2 = {name: age for (name, age) in zip(names, ages) if age >= 39}
print(new_dictionary_2)

population_result = {country: population for (country, population) in population_2.items() if population > 50}
print(population_result)

# Dictionary Comprehension with a string - {key: value for key, value in string if condition} 
text = "Hello Diego, how are you?"
unique = {c: c.upper() for c in text if c in "aeiou" }
print(unique)