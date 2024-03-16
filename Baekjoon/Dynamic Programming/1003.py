import sys

input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
n = max(numbers)
dp = [[0, 0] for _ in range(n + 1)]

dp[0] = [1, 0]
if n >= 1:
    dp[1] = [0, 1]
if n >= 2:
    dp[2] = [1, 1]

for i in range(3, n + 1):
    dp[i] = list(map(lambda x: sum(x), zip(dp[i - 1], dp[i - 2])))

print(*[f"{dp[i][0]} {dp[i][1]}" for i in numbers], sep = '\n')