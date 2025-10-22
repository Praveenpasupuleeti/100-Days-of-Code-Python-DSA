# Day 41 - DSA Practice Questions

# Product of Array Except Self (Array)
# Given an array nums, return an array output where output[i] is the product of all numbers except nums[i].
# Solve without using division and in O(n) time.
def product_except_self(nums):
    n = len(nums)
    left, right, result = [1]*n, [1]*n, [1]*n
    
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(n):
        result[i] = left[i] * right[i]
    return result

print(product_except_self([1,2,3,4]))  # Output: [24,12,8,6]


# Longest Substring Without Repeating Characters (String/Sliding Window)
# Find the length of the longest substring without repeating characters.
def length_of_longest_substring(s):
    seen = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")


# Rotate Matrix 90 Degrees (Matrix)
# Rotate a given n x n 2D matrix 90 degrees clockwise in place.
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))  # Output: [[7,4,1],[8,5,2],[9,6,3]]


# Find Missing Number (Math/Array)
# Given nums containing n distinct numbers from 0 to n, find the missing number.
def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

print(missing_number([3,0,1]))  # Output: 2


# Top K Frequent Elements (Heap/Hashing)
# Given an integer array nums and integer k, return the k most frequent elements.
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [num for num, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]

print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1,2]
