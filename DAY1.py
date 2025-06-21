# ------------------------------------------
# Day 1 - Problem 1: Odd or Even
# ------------------------------------------

# Take input from user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ------------------------------------------
# Day 1 - Problem 2: Positive, Negative, or Zero
# ------------------------------------------

# Take input from user
num = int(input("Enter a number: "))

# Check if positive, negative, or zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ------------------------------------------
# Day 1 - Problem 3: Simple Calculator
# ------------------------------------------

# Take input: 2 numbers and operator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
