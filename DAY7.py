# ------------------------------------------
# Day 7 - Problem Solving with Tuples & Sets
# ------------------------------------------

# ----------------------------------------
# Problem 1: Find Max and Min in a Tuple
# ----------------------------------------

def max_min_tuple(tup):
    return max(tup), min(tup)

nums = tuple(map(int, input("Problem 1 - Enter numbers separated by space: ").split()))
mx, mn = max_min_tuple(nums)
print(f"Max: {mx}, Min: {mn}")


# -----------------------------------------------
# Problem 2: Remove Duplicates Using Set
# -----------------------------------------------

def remove_duplicates(lst):
    return set(lst)

nums_list = list(map(int, input("\nProblem 2 - Enter list with duplicates: ").split()))
unique_set = remove_duplicates(nums_list)
print("Unique elements (as set):", unique_set)


# ------------------------------------------------------
# Problem 3: Find Common Elements Between Two Sets
# ------------------------------------------------------

def common_elements(set1, set2):
    return set1 & set2

set1 = set(map(int, input("\nProblem 3 - Enter elements of Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of Set 2 (space-separated): ").split()))

common = common_elements(set1, set2)
print("Common elements:", common)
