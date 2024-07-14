from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    cheeses = []

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True

                if matrix[next_v[0]][next_v[1]] == 0:
                    queue.append(next_v)
                else:
                    cheeses.append(next_v)

    return cheeses

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
time = 0
count = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]

    if not (cheeses := bfs((0, 0))):
        print(time)
        print(count)
        break
    else:
        count = len(cheeses)
        time += 1

        for cheese in cheeses:
            matrix[cheese[0]][cheese[1]] = 0