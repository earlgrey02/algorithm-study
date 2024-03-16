import sys

input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))

print(sum([sum(times[:i + 1]) for i in range(n)]))