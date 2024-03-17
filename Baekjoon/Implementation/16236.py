from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = 0
    fishes = []

    while queue:
        v = queue.popleft()

        if fishes and fishes[0][1] <= visited[v[0]][v[1]]:
            break

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and visited[next_v[0]][next_v[1]] == -1 and matrix[next_v[0]][next_v[1]] <= size:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1

                if 1 <= matrix[next_v[0]][next_v[1]] < size:
                    fishes.append((next_v, visited[next_v[0]][next_v[1]]))

                queue.append(next_v)

    return sorted(fishes, key = lambda x: (x[0][0], x[0][1]))

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
size = 2
exp = 0
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark = (i, j)
            matrix[i][j] = 0

while True:
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    fishes = bfs(shark)

    if not fishes:
        break

    v, w = fishes[0]
    matrix[v[0]][v[1]] = 0
    exp += 1
    answer += w
    shark = v

    if exp == size:
        exp = 0
        size += 1

print(answer)