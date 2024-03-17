from collections import deque
import sys

input = sys.stdin.readline

def topologicalSort():
    queue = deque([i for i in range(1, n + 1) if indegrees[i] == 0])

    while queue:
        v = queue.popleft()
        answer.append(v)

        for next_v in adj[v]:
            indegrees[next_v] -= 1

            if indegrees[next_v] == 0:
                queue.append(next_v)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indegrees = [0 for _ in range(n + 1)]
answer = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    indegrees[v2] += 1

topologicalSort()

print(*answer)