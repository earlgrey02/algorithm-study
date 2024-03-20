from math import inf
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
boards = []
answer = inf

for i in range(n - 7):
    for j in range(m - 7):
        boards.append([row[j:8 + j] for row in board[i:8 + i]])

for first in ('B', 'W'):
    for board in boards:
        cnt = 0

        for row in board:
            temp = first

            for color in row:
                if color != temp:
                    cnt += 1

                temp = 'B' if temp == 'W' else 'W'

            first = 'B' if first == 'W' else 'W'

        answer = min(answer, cnt)

print(answer)