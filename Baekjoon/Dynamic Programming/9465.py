import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n >= 2:
        dp[0][1] = dp[1][0] + dp[0][1]
        dp[1][1] = dp[0][0] + dp[1][1]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i + 1][j - 2], dp[i + 1][j - 1]) + dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 2], dp[i - 1][j - 1]) + dp[i][j]

    answer.append(max(map(max, dp)))

print(*answer, sep = '\n')