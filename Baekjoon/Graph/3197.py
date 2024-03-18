from collections import deque
import sys

input = sys.stdin.readline

def union(v1, v2):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v1[0]][v1[1]] == ranks[v2[0]][v2[1]]:
            parents[v2[0]][v2[1]] = v1
            ranks[v1[0]][v1[1]] += 1
        elif ranks[v1[0]][v1[1]] < ranks[v2[0]][v2[1]]:
            parents[v1[0]][v1[1]] = v2
        else:
            parents[v2[0]][v2[1]] = v1

def find(v):
    if parents[v[0]][v[1]] != v:
        parents[v[0]][v[1]] = find(parents[v[0]][v[1]])

    return parents[v[0]][v[1]]

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
parents = [[(i, j) for j in range(c)] for i in range(r)]
ranks = [[0 for _ in range(c)] for _ in range(r)]
swans = []
ices = deque()
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'L':
            swans.append((i, j))
            matrix[i][j] = '.'

for i in range(r):
    for j in range(c):
        if not visited[i][j] and matrix[i][j] == '.':
            queue = deque([(i, j)])
            visited[i][j] = True

            while queue:
                v = queue.popleft()

                for k in range(4):
                    next_v = (v[0] + dy[k], v[1] + dx[k])

                    if 0 <= next_v[0] < r and 0 <= next_v[1] < c and not visited[next_v[0]][next_v[1]]:
                        visited[next_v[0]][next_v[1]] = 1

                        if matrix[next_v[0]][next_v[1]] == '.':
                            union(v, next_v)
                            queue.append(next_v)
                        else:
                            ices.append(next_v)

while find(swans[0]) != find(swans[1]):
    nextIces = deque()

    while ices:
        v = ices.popleft()
        matrix[v[0]][v[1]] = '.'

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c:
                if matrix[next_v[0]][next_v[1]] == '.':
                    union(v, next_v)
                elif not visited[next_v[0]][next_v[1]] and matrix[next_v[0]][next_v[1]] == 'X':
                    visited[next_v[0]][next_v[1]] = True
                    nextIces.append(next_v)

    ices = nextIces
    answer += 1

print(answer)