# Topics: DFS (Number of Islands), BFS (Word Ladder length), Union-Find (connected components),
#        Longest Increasing Subsequence (n log n), Coin Change (DP - min coins)

from collections import deque, defaultdict
import bisect
from typing import List

# Problem 1: Number of Islands (DFS)
# Given a 2D grid of '1's (land) and '0's (water), count islands (connected vertically/horizontally).
# Time: O(m*n)

def num_islands(grid: List[List[str]]) -> int:
    if not grid: 
        return 0
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '#'  # mark visited
        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

g = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("1) Number of Islands:", num_islands([row[:] for row in g])) 

# Problem 2: Word Ladder (BFS shortest path in unweighted graph)
# Given beginWord, endWord and a wordList, return length of shortest transformation sequence.
# Time: O(M * N) roughly where M = word length, N = wordList size

from collections import deque
from typing import List

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    # BFS
    q = deque([(beginWord, 1)])
    visited = {beginWord}
    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
        # generate neighbors by changing one char
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                nxt = word[:i] + c + word[i+1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps+1))
    return 0

print("2) Word Ladder Length:", ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5


# ------------------------------
# Problem 3: Number of Connected Components in Undirected Graph (Union-Find)
# Given n nodes (0..n-1) and edges list, return count of connected components.
# Time: near O(alpha(n)) per union/find
# ------------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.count = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.count -= 1

def count_components(n: int, edges: List[List[int]]) -> int:
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count

print("3) Connected Components:", count_components(5, [[0,1],[1,2],[3,4]]))  # 2


# ------------------------------
# Problem 4: Longest Increasing Subsequence (n log n patience algorithm)
# Return length of LIS
# Time: O(n log n)
# ------------------------------
def length_of_lis(nums: List[int]) -> int:
    if not nums:
        return 0
    tails = []
    for x in nums:
        # find insertion position
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)

print("4) Length of LIS:", length_of_lis([10,9,2,5,3,7,101,18]))  # 4 (2,3,7,101)


# ------------------------------
# Problem 5: Coin Change (Minimum coins) - classic DP (unbounded)
# Given coins and amount, return fewest number of coins needed to make amount, or -1.
# Time: O(amount * len(coins))
# ------------------------------
def coin_change(coins: List[int], amount: int) -> int:
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a-c] + 1)
    return dp[amount] if dp[amount] <= amount else -1

print("5) Coin Change:", coin_change([1,2,5], 11))  # 3 (5+5+1)
