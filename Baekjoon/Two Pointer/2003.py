import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
left, right = 0, 0
sum = sequence[0]
answer = 0

while True:
    if sum == m:
        answer += 1

    if sum > m:
        sum -= sequence[left]
        left += 1
    else:
        right += 1

        if right >= n:
            break

        sum += sequence[right]

print(answer)