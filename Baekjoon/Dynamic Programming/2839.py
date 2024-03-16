import sys

input = sys.stdin.readline

n = int(input())
dp = [-1 for _ in range(n + 1)]

if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1

for i in range(6, n + 1):
    if dp[i - 3] != -1 and dp[i - 5] != -1:
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
    else:
        cnt = max(dp[i - 3] + 1, dp[i - 5] + 1)
        dp[i] = cnt if cnt != 0 else -1

print(dp[n])