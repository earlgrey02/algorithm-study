import sys

input = sys.stdin.readline

n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in square[i]] for i in range(n)]

dp[0][0] = square[0][0]
if n >= 2:
    dp[1] = [square[0][0] + square[1][i] for i in range(2)]

for i in range(2, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j]
        elif j == i:
            dp[i][j] = dp[i - 1][i - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

        dp[i][j] += square[i][j]

print(max(dp[-1]))