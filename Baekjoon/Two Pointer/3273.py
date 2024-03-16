import sys

input = sys.stdin.readline

n = int(input())
sequence = sorted(list(map(int, input().split())))
x = int(input())
left, right = 0, n - 1
answer = 0

while left < right:
    sum = sequence[left] + sequence[right]

    if sum > x:
        right -= 1
    elif sum < x:
        left += 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)