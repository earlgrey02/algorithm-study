from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for next_v in adj[v]:
            if visited[next_v] == 0:
                visited[next_v] = -visited[v]
                queue.append(next_v)
            elif visited[v] == visited[next_v]:
                return False

    return True

k = int(input())
answer = []

for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    isBipartite = "YES"

    for _ in range(e):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)

    for i in range(1, v + 1):
        if not visited[i] and not bfs(i):
            isBipartite = "NO"
            break

    answer.append(isBipartite)

print(*answer, sep = '\n')