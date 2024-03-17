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

def kruskal():
    global answer

    for v1, v2, w in edges:
        if find(v1) != find(v2):
            answer += w
            union(v1, v2)

v, e = map(int, input().split())

edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key = lambda x: x[2])
parents = [i for i in range(v + 1)]
ranks = [0 for i in range(v + 1)]
answer = 0

kruskal()

print(answer)