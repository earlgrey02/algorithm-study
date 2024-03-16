import sys

input = sys.stdin.readline

expressions = input().split('-')
answer = 0

for number in map(int, expressions[0].split('+')):
    answer += number

for expression in expressions[1:]:
    for number in map(int, expression.split('+')):
        answer -= number

print(answer)