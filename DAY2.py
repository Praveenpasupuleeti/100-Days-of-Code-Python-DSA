# ------------------------------------------
# Day 2 - Problem 1: Print First N Natural Numbers
# ------------------------------------------

N = int(input("Enter a number: "))
print("Natural numbers from 1 to", N, "are:")
for i in range(1, N + 1):
    print(i, end=' ')
print()  # for a newline


# ------------------------------------------
# Day 2 - Problem 2: Sum of N Natural Numbers
# ------------------------------------------

N = int(input("Enter a number: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print("Sum of first", N, "natural numbers is:", sum)

# Alternatively, using formula
# sum = N * (N + 1) // 2
# print("Sum is:", sum)


# ------------------------------------------
# Day 2 - Problem 3: Multiplication Table
# ------------------------------------------

num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
