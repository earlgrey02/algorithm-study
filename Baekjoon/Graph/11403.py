from math import inf
import sys

input = sys.stdin.readline

def floydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] == 1 and adj[k][j] == 1:
                    adj[i][j] = 1

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

floydWarshall()

for row in adj:
    print(*row)