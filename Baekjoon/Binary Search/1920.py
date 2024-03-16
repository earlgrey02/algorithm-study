from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
numbers_1 = sorted(list(map(int, input().split())))
m = int(input())
numbers_2 = list(map(int, input().split()))

print(*[int(bisect_left(numbers_1, i) != bisect_right(numbers_1, i)) for i in numbers_2], sep = '\n')