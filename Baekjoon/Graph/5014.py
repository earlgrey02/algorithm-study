from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v == g:
            return visited[v]

        for next_v in (v + u, v - d):
            if 0 < next_v <= f and visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [-1 for _ in range(f + 1)]

print(bfs(s))