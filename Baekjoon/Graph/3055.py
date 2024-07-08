from collections import deque
from math import inf
import sys

input = sys.stdin.readline

def waters_bfs(v):
    queue = deque(v)

    for i, j in v:
        water_visited[i][j] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] == '.' and water_visited[next_v[0]][next_v[1]] == -1:
                water_visited[next_v[0]][next_v[1]] = water_visited[v[0]][v[1]] + 1
                queue.append(next_v)

def hedgehog_bfs(v):
    queue = deque([v])
    hedgehog_visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        if v == bibber:
            return hedgehog_visited[v[0]][v[1]]

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and (water_visited[next_v[0]][next_v[1]] if water_visited[next_v[0]][next_v[1]] > -1 else inf) > hedgehog_visited[v[0]][v[1]] + 1 and matrix[next_v[0]][next_v[1]] in ('.', 'D') and hedgehog_visited[next_v[0]][next_v[1]] == -1:
                hedgehog_visited[next_v[0]][next_v[1]] = hedgehog_visited[v[0]][v[1]] + 1
                queue.append(next_v)

    return "KAKTUS"

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
hedgehog_visited = [[-1 for _ in range(c)] for _ in range(r)]
water_visited = [[-1 for _ in range(c)] for _ in range(r)]
hedgehog = [(i, j) for j in range(c) for i in range(r) if matrix[i][j] == 'S'][0]
bibber = [(i, j) for j in range(c) for i in range(r) if matrix[i][j] == 'D'][0]
waters = [(i, j) for j in range(c) for i in range(r) if matrix[i][j] == '*']
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

waters_bfs(waters)
print(hedgehog_bfs(hedgehog))