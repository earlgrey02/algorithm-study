import sys

input = sys.stdin.readline

def backtracking(v, depth):
    global answer

    answer = max(answer, depth)

    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] not in visited:
            visited.add(matrix[next_v[0]][next_v[1]])
            backtracking(next_v, depth + 1)
            visited.remove(matrix[next_v[0]][next_v[1]])

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = set([matrix[0][0]])
answer = 1
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

backtracking((0, 0), 1)

print(answer)