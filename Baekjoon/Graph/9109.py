from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    global b
    queue = deque([v])
    visited[v] = []

    while queue:
        v = queue.popleft()

        if v == b:
            return visited[v]

        for operator, next_v in (('D', v * 2 % 10000), ('S', (v - 1) % 10000), ('L', v // 1000 + (v % 1000) * 10), ('R', v // 10 + (v % 10) * 1000)):
            if 0 <= next_v < 10000 and visited[next_v] == None:
                visited[next_v] = [*visited[v], operator]
                queue.append(next_v)

t = int(input())
answer = []

for a, b in [map(int, input().split()) for _ in range(t)]:
    visited = [None for _ in range(10000)]
    answer.append(''.join(bfs(a)))

print(*answer, sep = '\n')