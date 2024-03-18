import sys

input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
dp = [0 for i in range(n + 1)]

dp[1] = wines[1]
if n >= 2:
    dp[2] = sum(wines[1:3])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + sum(wines[i - 1:i + 1]))

print(dp[n])