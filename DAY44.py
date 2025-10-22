# Topics: Sliding Window (deque), Sliding Window (char replacement), 3Sum, Valid Parentheses, Linked List Cycle (Floyd)
from collections import deque
from typing import List, Optional

# Problem 1: Sliding Window Maximum (deque)
# Given an array and window size k, return list of maximums for each sliding window.
# Time: O(n), Space: O(k)

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    if not nums or k == 0:
        return []
    dq = deque()  # store indices, decreasing values
    res = []
    for i, x in enumerate(nums):
        # pop left if out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # pop smaller values from right
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

print("1) Sliding Window Max:", sliding_window_max([1,3,-1,-3,5,3,6,7], 3))  # -> [3,3,5,5,6,7]


# Problem 2: Longest Repeating Character Replacement (Sliding window)
# Given a string s and int k, return max length of substring you can get by replacing <= k chars.
# Classic sliding-window with count of most frequent char.

def character_replacement(s: str, k: int) -> int:
    count = [0]*26
    maxf = 0
    left = 0
    res = 0
    for right in range(len(s)):
        idx = ord(s[right]) - ord('A')
        count[idx] += 1
        maxf = max(maxf, count[idx])
        # if window size - most_freq > k, shrink
        while (right - left + 1) - maxf > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

print("2) Char Replacement:", character_replacement("AABABBA", 1))  # -> 4



# Problem 3: 3Sum (Two Pointers)
# Return all unique triplets that sum to zero.
# Time: O(n^2)

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

print("3) 3Sum:", three_sum([-1,0,1,2,-1,-4]))  # -> [[-1,-1,2],[-1,0,1]]



# Problem 4: Valid Parentheses (Stack)
# Check if parentheses string is valid.

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack

print("4) Valid Parentheses ()[]{}:", is_valid_parentheses("()[]{}"))  # True
print("4) Valid Parentheses (]{):", is_valid_parentheses("([)]"))     # False



# Problem 5: Linked List Cycle Detection (Floyd's Tortoise and Hare)
# Return True if a cycle exists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

# Example: no cycle
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = None
print("5) Has Cycle (no):", has_cycle(n1))  # False

# Example: with cycle
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b; b.next = c; c.next = b   # cycle back to b
print("5) Has Cycle (yes):", has_cycle(a))  # True