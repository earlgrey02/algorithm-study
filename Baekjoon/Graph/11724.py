from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        for next_v in range(n):
            if matrix[v][next_v] and not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

n, m = map(int, input().split())

matrix = [[False for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    matrix[u][v] = True
    matrix[v][u] = True

for v in range(n):
    if not visited[v]:
        bfs(v)
        answer += 1

print(answer)