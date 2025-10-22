# Day 42 - Arrays & Strings (5 problems in one file)

from collections import Counter

# ------------------------------
# Problem 1: Move Zeroes to End
# In-place, one-pass, O(n) time, O(1) extra space.
# Example: [0,1,0,3,12] -> [1,3,12,0,0]
# ------------------------------

def move_zeroes(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
            last_non_zero += 1
    return nums

print("Move Zeroes:", move_zeroes([0,1,0,3,12]))


# ------------------------------
# Problem 2: Two Sum II - Input Array is Sorted
# Two-pointer approach, returns 1-based indices.
# Example: [2,7,11,15], target=9 -> [1,2]
# ------------------------------

def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

print("Two Sum Sorted:", two_sum_sorted([2,7,11,15], 9))


# ------------------------------
# Problem 3: Valid Anagram
# Use Counter (or sorting). Returns True/False.
# Example: "listen","silent" -> True
# ------------------------------

def is_anagram(s, t):
    return Counter(s) == Counter(t)

print("Is Anagram (listen/silent):", is_anagram("listen", "silent"))
print("Is Anagram (rat/car):", is_anagram("rat", "car"))


# ------------------------------
# Problem 4: Intersection of Two Arrays
# Return unique intersection (order not guaranteed).
# Example: [1,2,2,1], [2,2] -> [2]
# ------------------------------
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print("Intersection:", intersection([1,2,2,1], [2,2]))


# ------------------------------
# Problem 5: Best Time to Buy and Sell Stock
# Single pass, track min price and max profit.
# Example: [7,1,5,3,6,4] -> 5
# ------------------------------

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print("Max Profit:", max_profit([7,1,5,3,6,4]))
