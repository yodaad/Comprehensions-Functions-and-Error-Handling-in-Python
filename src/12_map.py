# Map function is used to apply a function to all the elements of specified iterable and return map object. Basically a map function executes the function on each item in the list.

numbers = [1, 2, 3, 4]
numbers2 = []

for i in numbers:
    numbers2.append(i * 2)

# Map function syntax - map(function, iterable). It returns a map object. Uses list to convert the map object to a list.
numbers3 = list(map(lambda i: i * 2, numbers))
   
print(numbers)
print(numbers2)
print(numbers3)

numbers1 = [1, 2, 3, 4]
numbers1_2 = [5, 6, 7]

print(numbers1)
print(numbers1_2)

# Map function with multiple iterables and lambda function.
result = list(map(lambda x, y: x + y, numbers1, numbers1_2))
print(result)

countries = ["col", "mex", "bol", "arg"]
countries2 = list(map(lambda country: country.upper(), countries))
print(countries)
print(countries2)