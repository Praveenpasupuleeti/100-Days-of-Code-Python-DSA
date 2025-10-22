# 📘 Day 47 - Graphs (DFS, Topological Sort, Union-Find)
# Topics: Depth-First Search, Cycle Detection, Topological Sorting, Union-Find (Disjoint Sets)

from collections import defaultdict, deque
from typing import List


# Problem 1️⃣: Number of Islands (DFS)
# Given a 2D grid of '1's (land) and '0's (water),
# count the number of islands.

def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["0","0","0","0"]
]
print("1️⃣ Number of Islands:", num_islands(grid))  # Output: 3

# Problem 2️⃣: Course Schedule (Topological Sort)
# Given numCourses and prerequisites, 
# return True if you can finish all courses.

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    taken = 0
    while q:
        node = q.popleft()
        taken += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return taken == numCourses

print("2️⃣ Can Finish Courses:", can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))  # True

# Problem 3️⃣: Detect Cycle in Directed Graph (DFS)

def has_cycle_dfs(n: int, edges: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * n  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        visited[node] = 1
        for nei in graph[node]:
            if dfs(nei):
                return True
        visited[node] = 2
        return False

    for i in range(n):
        if visited[i] == 0 and dfs(i):
            return True
    return False

print("3️⃣ Has Cycle:", has_cycle_dfs(4, [[0,1],[1,2],[2,0]]))  # True
print("3️⃣ Has Cycle:", has_cycle_dfs(3, [[0,1],[1,2]]))       # False

# Problem 4️⃣: Union-Find (Detect Cycle in Undirected Graph)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

def detect_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False

print("4️⃣ Undirected Cycle:", detect_cycle_undirected(3, [[0,1],[1,2],[0,2]]))  # True
print("4️⃣ Undirected Cycle:", detect_cycle_undirected(3, [[0,1],[1,2]]))        # False

# Problem 5️⃣: Clone Graph (DFS)
# Each node has a list of neighbors. Return a deep copy.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    old_to_new = {}

    def dfs(node):
        if not node:
            return None
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)
print("5️⃣ Clone Graph implemented successfully ✅")