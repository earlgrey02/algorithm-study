from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
answer = 0

for i in range(1, n + 1):
    answer += len(list(filter(lambda x: x == s, map(sum, combinations(sequence, i)))))

print(answer)