from math import inf
import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n, s = map(int, input().split())
    points = sorted(list(map(int, input().split())))
    start, end = 1, points[-1] - points[0]

    while start <= end:
        mid = (start + end) // 2
        current = points[0]
        cnt = 1

        for point in points[1:]:
            if point - current >= mid:
                cnt += 1
                current = point

        if cnt >= s:
            start = mid + 1
        else:
            end = mid - 1

    answer.append(end)

print(*answer, sep = '\n')