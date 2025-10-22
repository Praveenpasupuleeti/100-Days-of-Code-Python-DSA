# Topics: Rotated Binary Search, Floyd on array (duplicate), Backtracking (permutations),
# DP (Decode Ways), Heap (merge k sorted lists)

from typing import List
import heapq

# Problem 1: Search in Rotated Sorted Array (binary-search variant)
# Given a rotated sorted array (no duplicates), find index of target or -1.
# Time: O(log n)

def search_rotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # left half sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print("1) Rotated Search:", search_rotated([4,5,6,7,0,1,2], 0))  # -> 4
print("1) Rotated Search (not found):", search_rotated([4,5,6,7,0,1,2], 3))  # -> -1


# Problem 2: Find Duplicate Number (Floyd's Tortoise and Hare)
# Given array nums with n+1 integers where numbers in [1..n], find the duplicate.
# Time: O(n), Space: O(1)

def find_duplicate(nums: List[int]) -> int:
    # Phase 1: find intersection
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # Phase 2: find entrance to cycle
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

print("2) Find Duplicate:", find_duplicate([1,3,4,2,2]))  # -> 2
print("2) Find Duplicate:", find_duplicate([3,1,3,4,2]))  # -> 3


# Problem 3: Generate All Permutations (Backtracking)
# Given a list of unique numbers, return all permutations.
# Time: O(n * n!) output size

def permutations(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    used = [False]*n
    curr = []
    def backtrack():
        if len(curr) == n:
            res.append(curr.copy())
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            curr.append(nums[i])
            backtrack()
            curr.pop()
            used[i] = False
    backtrack()
    return res

print("3) Permutations:", permutations([1,2,3]))  # -> 6 permutations


# Problem 4: Decode Ways (DP)
# Given a string s containing digits, return number of ways to decode (1->A ... 26->Z).
# Example: "12" -> 2 ("AB","L")
# Time: O(n), Space: O(1)

def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    prev = 1   # ways to decode empty prefix
    curr = 1   # ways to decode prefix of length 1 (if not '0')
    for i in range(1, n):
        temp = 0
        if s[i] != '0':
            temp += curr
        two = int(s[i-1:i+1])
        if 10 <= two <= 26:
            temp += prev
        prev, curr = curr, temp
    return curr

print("4) Decode Ways (\"12\"):", num_decodings("12"))   # -> 2
print("4) Decode Ways (\"226\"):", num_decodings("226")) # -> 3
print("4) Decode Ways (\"0\"):", num_decodings("0"))     # -> 0


# ------------------------------
# Problem 5: Merge k Sorted Lists (min-heap)
# Given list of sorted lists, merge into one sorted list.
# Time: O(N log k) where N total elements, k lists
# ------------------------------
def merge_k_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    # push first element of each list with (value, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    res = []
    while heap:
        val, li_idx, el_idx = heapq.heappop(heap)
        res.append(val)
        if el_idx + 1 < len(lists[li_idx]):
            next_val = lists[li_idx][el_idx+1]
            heapq.heappush(heap, (next_val, li_idx, el_idx+1))
    return res

print("5) Merge k Lists:", merge_k_lists([[1,4,5],[1,3,4],[2,6]]))  # -> [1,1,2,3,4,4,5,6]