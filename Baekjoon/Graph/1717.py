import sys

sys.setrecursionlimit(10 ** 9)
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

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

for _ in range(m):
    operator, a, b = map(int, input().split())

    if operator == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")