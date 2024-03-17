from math import inf
import sys

input = sys.stdin.readline

def floydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) if i != j else 0

n, m = [int(input()) for _ in range(2)]
distance = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    distance[v1 - 1][v2 - 1] = min(distance[v1 - 1][v2 - 1], w)

floydWarshall()

for row in distance:
    print(*[i if i != inf else 0 for i in row])