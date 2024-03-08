from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 1 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

answer = []
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs((i, j))
                cnt += 1

    answer.append(cnt)

for cnt in answer:
    print(cnt)