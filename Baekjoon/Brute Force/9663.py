import sys

input = sys.stdin.readline

def backtracking(depth):
    global answer

    if depth == n:
        answer += 1
    else:
        for position in range(n):
            if not visited[position]:
                positions[depth] = position

                if isPossiblePosition(depth):
                    visited[position] = True
                    backtracking(depth + 1)
                    visited[position] = False

def isPossiblePosition(depth):
    for i in range(depth):
        if positions[depth] == positions[i] or abs(positions[depth] - positions[i]) == abs(depth - i):
            return False

    return True

n = int(input())
positions = [0 for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0

backtracking(0)

print(answer)