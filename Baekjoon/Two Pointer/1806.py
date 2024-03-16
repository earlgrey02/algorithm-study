from math import inf
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
left, right = 0, 0
sum = sequence[0]
answer = inf

while True:
    if sum >= s:
        answer = min(right - left + 1, answer)
        sum -= sequence[left]
        left += 1
    else:
        right += 1

        if right >= n:
            break

        sum += sequence[right]

print(answer if answer != inf else 0)