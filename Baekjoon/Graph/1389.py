from math import inf
import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

n, m = map(int, input().split())
distance = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(lambda x: int(x) - 1, input().split())
    distance[v1][v2] = 1
    distance[v2][v1] = 1

floyd_warshall()

print(min(enumerate(map(sum, distance)), key = lambda x: x[1])[0] + 1)