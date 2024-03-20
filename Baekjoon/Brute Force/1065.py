import sys

input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(1, n + 1):
    if i < 100 or (i < 1000 and int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1])):
        answer += 1

print(answer)