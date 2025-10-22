#  Day 49 - Dynamic Programming (Intermediate)
# Topics: 0/1 Knapsack, Subset Sum, Partition Equal Subset, Min Path Sum, Unique Paths


from typing import List

# Problem 1: 0/1 Knapsack Problem
# You have weights[] and values[], and a capacity W.
# Maximize total value without exceeding W.

def knapsack(weights: List[int], values: List[int], W: int) -> int:
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

print("1️ 0/1 Knapsack:", knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # 9


# Problem 2️: Subset Sum Problem
# Check if there exists a subset with a given sum.

def subset_sum(nums: List[int], target: int) -> bool:
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  # Sum 0 is always possible

    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if nums[i-1] <= s:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
            else:
                dp[i][s] = dp[i-1][s]

    return dp[n][target]

print("2️ Subset Sum Exists:", subset_sum([3, 34, 4, 12, 5, 2], 9))  # True


# Problem 3️: Partition Equal Subset Sum
# Can array be divided into two subsets with equal sum?

def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    return subset_sum(nums, total // 2)

print("3️ Can Partition Equal Subset:", can_partition([1, 5, 11, 5]))  # True


# Problem 4️: Minimum Path Sum (Grid DP)
# Find minimum path sum from top-left to bottom-right in grid.

def min_path_sum(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # Fill first row and column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill rest
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("4️ Minimum Path Sum:", min_path_sum(grid))  # 7


# Problem 5️: Unique Paths in a Grid (Combinatorial DP)
# Move only right or down.

def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

print("5️ Unique Paths:", unique_paths(3, 7))  # 28
