import sys

input = sys.stdin.readline

n, k = map(int, input().split())
days = list(map(int, input().split()))
left, right = 0, k - 1
sum = sum(days[left:right + 1])
answer = sum

while True:
    sum -= days[left]
    left += 1
    right += 1

    if right >= n:
        break

    sum += days[right]

    answer = max(answer, sum)

print(answer)