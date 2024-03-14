import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    for next_v in adj[v]:
        if visited[next_v] == -1:
            visited[next_v] = v
            dfs(next_v)

n = int(input())
adj = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visited[1] = 0
dfs(1)

print(*visited[2:], sep = "\n")