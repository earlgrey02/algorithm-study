from collections import deque
from copy import deepcopy
import heapq
import sys

input = sys.stdin.readline

def dfs(v, visited):
    print(v, end = " ")
    visited[v] = True

    for next_v in adj[v]:
        if not visited[next_v]:
            dfs(next_v, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for next_v in adj[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(n + 1):
    adj[i].sort()

dfs(v, deepcopy(visited))
print()
bfs(v, deepcopy(visited))