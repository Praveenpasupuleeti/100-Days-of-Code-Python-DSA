# Topics: Memoization, Tabulation, Fibonacci, Climbing Stairs, Coin Change, LCS

from typing import List

# Problem 1️⃣: Fibonacci (Top-Down Memoization)

def fib_memo(n: int, memo={}) -> int:
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print("1️⃣ Fibonacci (Memoization):", fib_memo(10))  # 55

# Problem 2️⃣: Fibonacci (Bottom-Up Tabulation)

def fib_tab(n: int) -> int:
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print("2️⃣ Fibonacci (Tabulation):", fib_tab(10))  # 55

# Problem 3️⃣: Climbing Stairs
# You can climb 1 or 2 steps at a time.
# Find total distinct ways to reach top.

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print("3️⃣ Climbing Stairs:", climb_stairs(5))  # 8

# Problem 4️⃣: Coin Change (Minimum Coins)
# Given coins[] and amount, return min coins to make amount.

def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print("4️⃣ Coin Change:", coin_change([1, 2, 5], 11))  # 3 (5+5+1)

# Problem 5️⃣: Longest Common Subsequence (LCS)

def lcs(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

print("5️⃣ Longest Common Subsequence:", lcs("abcde", "ace"))  # 3 ("ace")

# Problem 6️⃣: House Robber
# Adjacent houses cannot be robbed.

def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[-1]

print("6️⃣ House Robber:", rob([2, 7, 9, 3, 1]))  # 12 (7+3+2)