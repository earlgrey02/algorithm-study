from itertools import combinations
from math import inf
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
houses = [(i, j) for j in range(n) for i in range(n) if matrix[i][j] == 1]
chickens = [(i, j) for j in range(n) for i in range(n) if matrix[i][j] == 2]
answer = []

for chickens in combinations(chickens, m):
    total = 0

    for house in houses:
        distance = inf

        for chicken in chickens:
            distance = min(distance, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))

        total += distance

    answer.append(total)

print(min(answer))