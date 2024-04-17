"""Lambda Functions are small anonymous functions that can have any number of arguments, but can only have one expression. 
They are used when you need a short function for a short period of time. """
import datetime

def increment(x):
    return x + 1

result = increment(10)
print(result)

# Lambda Function Syntax is lambda arguments: expression, it can have any number of arguments, but only one expression.
increment_2 = lambda x: x + 1

result = increment_2(20)
print(result)

# Lambda Function with multiple arguments and expression that returns a string.
full_name_and_age = lambda name, last_name, age: f"Your full name is {name.title()} {last_name.title()}, and you are {age}, old." 
current_year = datetime.datetime.today().year

name= input("Enter your name: ")
last_name = input("Enter your last name: ")
year_of_birth = int(input("Enter the year you were born: "))
age = current_year - year_of_birth

text = full_name_and_age(name, last_name, age)
print(text)