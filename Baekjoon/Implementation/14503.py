import sys

input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
v = (y, x)
answer = 0
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

while True:
    isRotate = False

    if matrix[v[0]][v[1]] == 0:
        matrix[v[0]][v[1]] = -1
        answer += 1

    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0:
            d = d - 1 if d > 0 else 3
            isRotate = True
            next_v = (v[0] + dy[d], v[1] + dx[d])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0:
                v = next_v

            break

    if not isRotate:
        i = d - 2 if d > 1 else d + 2
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] != 1:
            v = next_v
        else:
            break

print(answer)