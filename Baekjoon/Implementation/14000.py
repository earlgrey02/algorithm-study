from itertools import combinations
import sys

input = sys.stdin.readline

def backtracking(v, sum, depth):
    global answer

    if depth == 4:
        answer = max(answer, sum)
    else:
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                backtracking(next_v, sum + matrix[next_v[0]][next_v[1]], depth + 1)
                visited[next_v[0]][next_v[1]] = False

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        backtracking((i, j), matrix[i][j], 1)
        visited[i][j] = False

        for directions in combinations(range(4), 3):
            temp = matrix[i][j]

            for d in directions:
                next_v = (i + dy[d], j + dx[d])

                if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                    temp += matrix[next_v[0]][next_v[1]]

            answer = max(answer, temp)

print(answer)