"""Error handling in Python can be done using the try, except, else, and finally keywords.
If an exception is raised, the code inside the try block stops executing and the control is transferred to the except block."""

# Try block - The code that can raise an exception is placed inside the try block.
try:
    print( 0 / 0)

# Except block - The code that handles the exception is placed inside the except block.
except ZeroDivisionError as error:
    print(error) 

# AssertionError - assert keyword is used to check if a condition is True. If the condition is False, the program will raise an AssertionError.
try: 
    assert 1 != 1, "One is not equal to one."
except AssertionError as error:
    print(error)

print("Hello")

# Try block with else block - The else block is executed if no exception is raised.
def password_validation(password):
    if password != "1234abcd":
        raise Exception("Wrong password!")

while True: 
    try:
            user_password = input("Enter your password: ")
            password_validation(user_password)       
    except Exception as error:
        print(error)       
    else:
        print("Welcome to the division tester!")
        break

# Try block with finally block - The finally block is executed regardless of whether an exception is raised or not.
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result:.2f}")
finally:
    print("Execution terminated.")
    
