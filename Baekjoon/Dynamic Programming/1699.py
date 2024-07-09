from math import inf
import sys

input = sys.stdin.readline

n = int(input())
dp = [inf for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    cases = []
    j = 1

    while j ** 2 <= i:
        cases.append(dp[i - j ** 2] + 1)
        j += 1

    dp[i] = min(cases)

print(dp[n])