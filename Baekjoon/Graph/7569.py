from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque(v)

    while queue:
        v = queue.popleft()

        for i in range(6):
            next_v = (v[0] + dz[i], v[1] + dy[i], v[2] + dx[i])

            if 0 <= next_v[0] < h and 0 <= next_v[1] < n and 0 <= next_v[2] < m and visited[next_v[0]][next_v[1]][next_v[2]] == -1 and matrix[next_v[0]][next_v[1]][next_v[2]] == 0:
                visited[next_v[0]][next_v[1]][next_v[2]] = visited[v[0]][v[1]][v[2]] + 1
                matrix[next_v[0]][next_v[1]][next_v[2]] = 1
                queue.append(next_v)

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
tomatoes = [(i, j, k) for k in range(m) for j in range(n) for i in range(h) if matrix[i][j][k] == 1]
dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dx = (0, 0, 0, 0, 1, -1)

for v in tomatoes:
    visited[v[0]][v[1]][v[2]] = 0

bfs(tomatoes)

if [True for k in range(m) for j in range(n) for i in range(h) if matrix[i][j][k] == 0]:
    print(-1)
else:
    answer = max(map(lambda x: max(map(max, x)), visited))
    print(answer if answer >= 0 else 0)