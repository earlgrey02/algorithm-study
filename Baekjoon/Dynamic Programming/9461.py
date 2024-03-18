import sys

input = sys.stdin.readline

t = int(input())
dp = [1 for _ in range(101)]
answer = []

for i in range(4, 101):
    dp[i] = sum(dp[i - 3:i - 1])

for _ in range(t):
    n = int(input())
    answer.append(dp[n])

print(*answer, sep = '\n')