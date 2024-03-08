import sys

input = sys.stdin.readline

def dfs(v):
    for next_v, w in matrix[v]:
        if visited[next_v] == -1:
            visited[next_v] = visited[v] + w
            dfs(next_v)

n = int(input())
matrix = [[] for _ in range(n + 1)]

for _ in range(n):
    numbers = list(map(int, input().split()))

    v = numbers[0]
    i = 1

    while True:
        e = numbers[i]

        if e == -1:
            break

        w = numbers[i + 1]
        matrix[v].append((e, w))
        i += 2

visited = [-1 for _ in range(n + 1)]
visited[1] = 0
dfs(1)
max_v = visited.index(max(visited))

visited = [-1 for _ in range(n + 1)]
visited[max_v] = 0
dfs(max_v)

print(max(visited))
