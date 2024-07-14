from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
l = int(input())
actions = [tuple(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(l)]
head = (0, 0)
bodies = deque([])
direction = 0
answer = 0
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

while True:
    isFinished = False
    answer += 1
    next_head = (head[0] + dy[direction], head[1] + dx[direction])

    if 0 <= next_head[0] < n and 0 <= next_head[1] < n and next_head not in bodies:
        if next_head in apples:
            apples.remove(next_head)
            bodies.append(head)
        elif bodies:
            bodies.popleft()
            bodies.append(head)

        head = next_head
    else:
        isFinished = True
        break

    if action := tuple(filter(lambda x: x[0] == answer, actions)):
        direction = (direction + 1) % 4 if action[0][1] == 'D' else (direction - 1) % 4

print(answer)