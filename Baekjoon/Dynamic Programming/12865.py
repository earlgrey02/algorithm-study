import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

for item in items:
    for i in range(k, 0, -1):
        if i < item[0]:
            break
        else:
            dp[i] = max(dp[i], dp[i - item[0]] + item[1])

print(dp[k])