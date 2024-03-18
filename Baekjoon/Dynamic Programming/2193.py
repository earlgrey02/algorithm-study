import sys

input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(2)] for _ in range(n)]

dp[0] = [0, 1]
if n >= 2:
    dp[1] = [1, 0]

for i in range(2, n):
    dp[i][0] = sum(dp[i - 1][:])
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n - 1]))