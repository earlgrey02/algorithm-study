import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = 0

for coin in coins[::-1]:
    answer += k // coin
    k %= coin

print(answer)