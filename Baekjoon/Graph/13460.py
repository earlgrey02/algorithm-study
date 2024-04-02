from collections import deque
import sys

input = sys.stdin.readline

def bfs(red_v, blue_v):
    queue = deque([(red_v, blue_v)])
    visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] = 0

    while queue:
        red_v, blue_v = queue.popleft()

        if visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] > 10:
            return -1
        elif matrix[red_v[0]][red_v[1]] == 'O':
            return visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]]

        for i in range(4):
            red_distance, blue_distance = 0, 0
            red_nv, blue_nv = red_v, blue_v

            while matrix[red_nv[0]][red_nv[1]] != 'O':
                red_nv = (red_nv[0] + dy[i], red_nv[1] + dx[i])
                red_distance += 1

                if matrix[red_nv[0]][red_nv[1]] == '#':
                    red_nv = (red_nv[0] - dy[i], red_nv[1] - dx[i])
                    red_distance -= 1
                    break

            while matrix[blue_nv[0]][blue_nv[1]] != 'O':
                blue_nv = (blue_nv[0] + dy[i], blue_nv[1] + dx[i])
                blue_distance += 1

                if matrix[blue_nv[0]][blue_nv[1]] == '#':
                    blue_nv = (blue_nv[0] - dy[i], blue_nv[1] - dx[i])
                    blue_distance -= 1
                    break

            if matrix[blue_nv[0]][blue_nv[1]] != 'O':
                if red_nv == blue_nv:
                    if red_distance > blue_distance:
                        red_nv = (red_nv[0] - dy[i], red_nv[1] - dx[i])
                    else:
                        blue_nv = (blue_nv[0] - dy[i], blue_nv[1] - dx[i])

                if visited[red_nv[0]][red_nv[1]][blue_nv[0]][blue_nv[1]] == -1:
                    visited[red_nv[0]][red_nv[1]][blue_nv[0]][blue_nv[1]] = visited[red_v[0]][red_v[1]][blue_v[0]][blue_v[1]] + 1
                    queue.append((red_nv, blue_nv))

    return -1

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            red_v = (i, j)
        elif matrix[i][j] == 'B':
            blue_v = (i, j)

print(bfs(red_v, blue_v))