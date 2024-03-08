from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque(v)

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < row and 0 <= next_v[1] < column and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                matrix[next_v[0]][next_v[1]] = 1
                queue.append(next_v)

column, row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
visited = [[0 for _ in range(column)] for _ in range(row)]
tomatoes = [(i, j) for i in range(row) for j in range(column) if matrix[i][j] == 1]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

bfs(tomatoes)

if [0 for i in range(row) for j in range(column) if matrix[i][j] == 0]:
    answer = -1
else:
    answer = max(map(max, visited))

print(answer)