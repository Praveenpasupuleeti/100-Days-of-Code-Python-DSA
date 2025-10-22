# Topics: Binary Search variants, Two Pointers, Hashmap (subarray sum), In-place merge

from typing import List

# ------------------------------
# Problem 1: Binary Search (Classic)
# Given a sorted array and a target, return the index of target or -1 if not found.
# ------------------------------
def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Quick tests
print("Problem 1 - Binary Search:", binary_search([1,3,5,7,9], 5))   # 2
print("Problem 1 - Binary Search (not found):", binary_search([1,3,5], 2))  # -1


# ------------------------------
# Problem 2: First and Last Position of Element in Sorted Array
# Return [first_index, last_index] or [-1, -1] if not present
# Uses two binary searches (lower bound and upper bound)
# ------------------------------
def find_first_last(nums: List[int], target: int) -> List[int]:
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(True)
    if first == -1:
        return [-1, -1]
    last = find_bound(False)
    return [first, last]
print("Problem 2 - First/Last:", find_first_last([5,7,7,8,8,10], 8))  # [3,4]
print("Problem 2 - First/Last (not found):", find_first_last([5,7,7,8,8,10], 6))  # [-1,-1]


# ------------------------------
# Problem 3: Container With Most Water (Two Pointers)
# Given heights array, find max area container (two-pointer greedy)
# ------------------------------
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, h * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
print("Problem 3 - Max Area:", max_area([1,8,6,2,5,4,8,3,7]))  # 49


# ------------------------------
# Problem 4: Subarray Sum Equals K (Hashmap prefix sums)
# Return number of continuous subarrays that sum to k.
# ------------------------------
def subarray_sum(nums: List[int], k: int) -> int:
    prefix_count = {0: 1}
    cur = 0
    ans = 0
    for x in nums:
        cur += x
        ans += prefix_count.get(cur - k, 0)
        prefix_count[cur] = prefix_count.get(cur, 0) + 1
    return ans
print("Problem 4 - Subarray Sum Equals K:", subarray_sum([1,1,1], 2))  # 2
print("Problem 4 - Subarray Sum K (negatives):", subarray_sum([1,-1,0], 0))  # 3


# ------------------------------
# Problem 5: Merge Sorted Arrays In-place (LeetCode style)
# Merge nums2 into nums1 which has buffer at the end. Assume nums1 length = m + n.
# Example: nums1=[1,2,3,0,0,0], m=3; nums2=[2,5,6], n=3 -> nums1 becomes [1,2,2,3,5,6]
# ------------------------------
def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    write = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1
a = [1,2,3,0,0,0]
merge_sorted(a, 3, [2,5,6], 3)
print("Problem 5 - Merged nums1:", a)  # [1,2,2,3,5,6]