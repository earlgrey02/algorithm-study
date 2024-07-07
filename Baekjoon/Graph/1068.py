import sys

input = sys.stdin.readline

def dfs(v):
    global deleted_v, answer
    visited[v] = True
    isLeaf = True

    for next_v in adj[v]:
        if not visited[next_v] and next_v != deleted_v:
            isLeaf = False
            dfs(next_v)

    if isLeaf:
        answer += 1

n = int(input())
adj = [[] for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0

for v1, v2 in enumerate(map(int, input().split())):
    if v2 == -1:
        root = v1
    else:
        adj[v2].append(v1)

deleted_v = int(input())

if root != deleted_v:
    dfs(root)

print(answer)