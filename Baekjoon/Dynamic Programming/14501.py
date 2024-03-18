import sys

input = sys.stdin.readline

n = int(input())
times = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 2)]

for i in range(1, n + 1):
    if i + times[i][0] < n + 2:
        dp[i + times[i][0]] = max(dp[i + times[i][0]], max(dp[:i + 1]) + times[i][1])

print(max(dp))