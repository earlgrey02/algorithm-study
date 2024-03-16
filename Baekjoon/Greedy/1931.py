from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
meetings = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
end = meetings[0][1]
answer = 1

for meeting in meetings[1:]:
    if meeting[0] >= end:
        answer += 1
        end = meeting[1]

print(answer)