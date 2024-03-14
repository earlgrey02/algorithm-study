from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and not visited[next_v[0]][next_v[1]] and matrix[v[0]][v[1]] == matrix[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
answers = [0, 0]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs((i, j))
            answers[0] += 1

matrix = [[matrix[i][j] if matrix[i][j] != "G" else "R" for j in range(n)] for i in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs((i, j))
            answers[1] += 1

print(*answers)