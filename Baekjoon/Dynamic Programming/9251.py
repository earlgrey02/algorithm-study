import sys

input = sys.stdin.readline

sequence_1, sequence_2 = [input().strip() for _ in range(2)]
dp = [[0 for _ in range(len(sequence_2) + 1)] for _ in range(len(sequence_1) + 1)]

for i in range(1, len(sequence_1) + 1):
    for j in range(1, len(sequence_2) + 1):
        if sequence_1[i - 1] == sequence_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])