import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1 if i == j or j == 0 else 0 for j in range(k + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[n][k])