# ----------------------------------------------
# Day 15 - Python Exception Handling Examples
# ----------------------------------------------

# -------------------------------
# Problem 1: Handle ZeroDivisionError
# -------------------------------

def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

print("Problem 1 - Division with Exception Handling")
divide_numbers()


# -------------------------------
# Problem 2: Handle ValueError for Input Conversion
# -------------------------------

def get_integer_input():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Error: Please enter a valid integer.")

print("\nProblem 2 - Input Validation")
get_integer_input()


# -------------------------------
# Problem 3: Raise Custom Exception
# -------------------------------

class UnderAgeError(Exception):
    pass

def check_age(age):
    try:
        if age < 18:
            raise UnderAgeError("You must be at least 18 years old.")
        else:
            print("Access granted.")
    except UnderAgeError as e:
        print("Access denied:", e)

print("\nProblem 3 - Custom Exception for Age Restriction")
check_age(16)  # Try with different ages
