# ------------------------------------------
# Day 3 - Problem 1: Find Maximum in a List
# ------------------------------------------

# Take list input
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum number is:", maximum)


# ------------------------------------------
# Day 3 - Problem 2: Count Even and Odd Numbers
# ------------------------------------------

# Take list input
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Count even and odd
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)


# ------------------------------------------
# Day 3 - Problem 3: Reverse a List
# ------------------------------------------

# Take list input
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Reverse using slicing
reversed_list = numbers[::-1]

print("Original List:", numbers)
print("Reversed List:", reversed_list)
