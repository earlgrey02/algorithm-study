from math import inf
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
apps = [0] + list(zip(*[list(map(int, input().split())) for _ in range(2)]))
k = sum(map(lambda x: x[1], apps[1:]))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
answer = inf

for i in range(1, n + 1):
    for j in range(k + 1):
        if apps[i][1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - apps[i][1] if j > 0 else 0] + apps[i][0])

        if dp[i][j] >= m:
            answer = min(answer, j)

print(answer)