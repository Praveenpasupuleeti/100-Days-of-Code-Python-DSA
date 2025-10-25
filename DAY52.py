# Day 52 - Advanced Stack & Queue Problems

from collections import deque, OrderedDict
from typing import List


# Problem 1: Min Stack
# Design a stack that supports push, pop, top, and retrieving minimum in O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(1)
min_stack.pop()
print("1) Current Min:", min_stack.get_min())  # 2


# Problem 2: Daily Temperatures (Monotonic Stack)
# For each day, find how many days until a warmer temperature
def daily_temperatures(temps: List[int]) -> List[int]:
    res = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res

print("2) Daily Temperatures:", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]


# Problem 3: Evaluate Reverse Polish Notation (Postfix)
# Input: tokens = ["2","1","+","3","*"] => ((2+1)*3)=9
def eval_rpn(tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': stack.append(int(a / b))
    return stack[0]

print("3) Evaluate RPN:", eval_rpn(["2", "1", "+", "3", "*"]))  # 9


# Problem 4: LRU Cache Implementation (OrderedDict)
# LRU = Least Recently Used cache eviction policy
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print("4) Get(1):", lru.get(1))  # 1
lru.put(3, 3)
print("4) Get(2):", lru.get(2))  # -1 (evicted)


# Problem 5: Sliding Window Maximum
# For every window of size k, find the maximum element
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq, res = deque(), []
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

print("5) Sliding Window Max:", max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
