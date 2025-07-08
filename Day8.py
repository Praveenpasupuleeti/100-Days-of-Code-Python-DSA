# ---------------------------------------------------
# Day 8 - Problem Solving: List Comprehension & Lambda
# ---------------------------------------------------

from functools import reduce

# ------------------------------------------
# Problem 1: Generate Squares using List Comprehension
# ------------------------------------------

N = int(input("Problem 1 - Enter a number: "))
squares = [x**2 for x in range(1, N + 1)]
print("Squares from 1 to", N, ":", squares)


# ---------------------------------------------------
# Problem 2: Filter Even Numbers using Lambda & filter
# ---------------------------------------------------

nums = list(map(int, input("\nProblem 2 - Enter a list of numbers: ").split()))
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_nums)


# ------------------------------------------------------------------
# Problem 3: Multiply All Elements using Lambda & functools.reduce
# ------------------------------------------------------------------

nums2 = list(map(int, input("\nProblem 3 - Enter a list of numbers to multiply: ").split()))
product = reduce(lambda x, y: x * y, nums2)
print("Product of all elements:", product)
