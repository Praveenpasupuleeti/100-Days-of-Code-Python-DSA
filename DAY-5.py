# ------------------------------------------
# Day 5 - Problem 1: Check Prime Number
# ------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")


# ------------------------------------------
# Day 5 - Problem 2: Factorial Function
# ------------------------------------------

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number to find factorial: "))
print("Factorial:", factorial(num))


# ------------------------------------------
# Day 5 - Problem 3: Largest Among Three Numbers
# ------------------------------------------

def find_largest(a, b, c):
    return max(a, b, c)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

largest = find_largest(x, y, z)
print("Largest number is:", largest)
