from math import sqrt
import sys

input = sys.stdin.readline

n = int(input())
primes = [True for _ in range(n + 1)]
primes[1] = False

for i in range(2, int(sqrt(n)) + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

sequence = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(primes))))
left, right = 0, 0
sum = sequence[0]
answer = 0

while True:
    if sum > n:
        sum -= sequence[left]
        left += 1
    elif sum < n:
        right += 1

        if right >= len(sequence):
            break

        sum += sequence[right]
    else:
        answer += 1
        sum -= sequence[left]
        left += 1
        right += 1

        if right >= len(sequence):
            break

        sum += sequence[right]

print(answer)