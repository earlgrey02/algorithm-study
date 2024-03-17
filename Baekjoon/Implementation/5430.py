from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    p = input().strip()
    n = int(input())
    array = deque(input().strip()[1:-1].split(','))

    if n == 0:
        array = deque()

    isError = False
    reverse = 0

    for func in p:
        if func == 'R':
            reverse += 1
        else:
            if len(array) == 0:
                isError = True
                break
            elif reverse % 2 == 0:
                array.popleft()
            else:
                array.pop()
    if isError:
        answer.append("error")
    else:
        if reverse % 2 != 0:
            array.reverse()

        answer.append(f"[{','.join(array)}]")

print(*answer, sep = '\n')