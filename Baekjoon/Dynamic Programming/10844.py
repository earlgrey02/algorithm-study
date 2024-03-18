import sys

input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]

dp[0] = [0] + [1 for _ in range(9)]

for i in range(1, n):
    for j in range(10):
        if j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        elif j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

        dp[i][j] %= 10 ** 9

print(sum(dp[n - 1]) % 10 ** 9)