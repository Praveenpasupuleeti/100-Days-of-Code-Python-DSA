# Day 50 - DSA Practice Problems

from typing import List

# Problem 1: Find Pair with Given Sum in Sorted Array
# Given a sorted array and a target, return the pair that sums to the target.
def two_sum_sorted(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [nums[left], nums[right]]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

print("1) Pair with sum:", two_sum_sorted([1, 2, 3, 4, 6, 8, 9], 10))  # [2,8]


# Problem 2: Search Insert Position
# Return the index where target should be inserted in sorted order.
def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print("2) Search Insert Position:", search_insert([1, 3, 5, 6], 5))  # 2
print("2) Insert Position (missing):", search_insert([1, 3, 5, 6], 2))  # 1


# Problem 3: Longest Subarray with Sum K (HashMap + Prefix Sum)
# Return the length of the longest subarray whose sum equals K.
def longest_subarray_sum(nums: List[int], k: int) -> int:
    prefix_sum = {0: -1}
    s = 0
    max_len = 0
    for i, num in enumerate(nums):
        s += num
        if s - k in prefix_sum:
            max_len = max(max_len, i - prefix_sum[s - k])
        if s not in prefix_sum:
            prefix_sum[s] = i
    return max_len

print("3) Longest Subarray with Sum K:", longest_subarray_sum([1, -1, 5, -2, 3], 3))  # 4


# Problem 4: Minimum Size Subarray Sum (Sliding Window)
# Find smallest length of subarray with sum >= target.
def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    total = 0
    min_len = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

print("4) Min Subarray Len:", min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2


# Problem 5: Find Peak Element (Binary Search)
# A peak element is greater than its neighbors. Return its index.
def find_peak(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

print("5) Peak Element Index:", find_peak([1, 2, 1, 3, 5, 6, 4]))  # 5
