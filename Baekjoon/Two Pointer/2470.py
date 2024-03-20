from math import inf
import sys

input = sys.stdin.readline

n = int(input())
solutions = sorted(list(map(int, input().split())))
left, right = 0, n - 1
answer = (inf, (inf, inf))

while left < right:
    value = solutions[left] + solutions[right]

    if abs(value) < answer[0]:
        answer = (abs(value), (solutions[left], solutions[right]))

    if value > 0:
        right -= 1
    else:
        left += 1

print(*answer[1])