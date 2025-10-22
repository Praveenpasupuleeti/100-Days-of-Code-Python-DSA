# Day 40 - DSA Practice Questions

# 1️⃣ Two Sum Problem (Medium, Array/Hashing)
# Given an array of integers, return indices of two numbers such that they add up to a specific target.
# Approach: Use hashmap for O(n) solution.
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

print(two_sum([2,7,11,15], 9))  # Output: [0,1]

# 2️⃣ Reverse Linked List (Medium, Linked List)
# Reverse a singly linked list iteratively.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3)))
rev_head = reverse_list(head)
while rev_head:
    print(rev_head.val, end=" ")  # Output: 3 2 1
    rev_head = rev_head.next

# 3️⃣ Valid Parentheses (Medium, Stack)
# Check if parentheses string is valid.
def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False

# 4️⃣ Merge Intervals (Medium, Array)
# Given intervals, merge all overlapping intervals.
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[1]:
            merged.append(interval)
        elif merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]

# 5️⃣ Kth Largest Element in Array (Medium, Heap)
# Find the kth largest element in an unsorted array.
import heapq
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(find_kth_largest([3,2,1,5,6,4], 2))  # Output: 5
