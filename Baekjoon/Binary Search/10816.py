from bisect import bisect_left, bisect_right
import sys

n = int(input())
owns = sorted(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))

print(*[bisect_right(owns, i) - bisect_left(owns, i) for i in cards])