import sys

input = sys.stdin.readline

def union(v1, v2):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v1] == ranks[v2]:
            parents[v2] = v1
            ranks[v1] += 1
        elif ranks[v1] < ranks[v2]:
            parents[v1] = v2
        else:
            parents[v2] = v1

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

n, m = [int(input()) for _ in range(2)]
adj = [list(map(int, input().split())) for _ in range(n)]
parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]


for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            union(i, j)

print("YES" if len(set(map(lambda x: find(int(x) - 1), input().split()))) == 1 else "NO")