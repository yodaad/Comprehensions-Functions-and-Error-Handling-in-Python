# Map function is used to apply a function to all the elements of specified iterable and return map object.

numbers = [1, 2, 3, 4]
numbers_2 = []

for i in numbers:
    numbers_2.append(i * 2)

numbers_3 = list(map(lambda i: i * 2, numbers))
   
print(numbers)
print(numbers_2)
print(numbers_3)

numbers_1 = [1, 2, 3, 4]
numbers_1_2 = [5, 6, 7]

print(numbers_1)
print(numbers_1_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_1_2))
print(result)
