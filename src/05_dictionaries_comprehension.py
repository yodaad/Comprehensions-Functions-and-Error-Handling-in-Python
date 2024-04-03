# Dictionaries Comprehension in Python is a way to build a new dictionary by applying an expression to each item in an iterable. 

import random

dictionary = {}
for i in range (1, 5):
    dictionary[i] = i * 2

print(dictionary)

dictionary_2 = {i: i * 2 for i in range (1, 5)}
print(dictionary_2)

countries = ["col", "mex", "bol", "per"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

population_2 = {country: random.randint(1, 100) for country in countries }
print(population_2)

names = ["Diego", "Dann", "Mike"]
ages = [39, 45, 21]

persons = list(zip(names, ages))
print(persons)

new_dictionary = {name: age for (name, age) in zip(names, ages) }
print(new_dictionary)


new_dictionary_2 = {name: age for (name, age) in zip(names, ages) if age >= 39}
print(new_dictionary_2)

population_result = {country: population for (country, population) in population_2.items() if population > 50}
print(population_result)

text = "Hello Diego, how are you?"
unique = {c: c.upper() for c in text if c in "aeiou" }
print(unique)