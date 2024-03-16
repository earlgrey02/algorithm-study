from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        if v == destination:
            return visited[v[0]][v[1]]

        for i in range(8):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < l and 0 <= next_v[1] < l and visited[next_v[0]][next_v[1]] == -1:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)


t = int(input())
answer = []
dy = (2, 2, -2, -2, 1, 1, -1, -1)
dx = (1, -1, 1, -1, 2, -2, 2, -2)

for _ in range(t):
    l = int(input())
    v, destination = [tuple(map(int, input().split())) for _ in range(2)]
    visited = [[-1 for _ in range(l)] for _ in range(l)]

    answer.append(bfs(v))

print(*answer, sep = '\n')