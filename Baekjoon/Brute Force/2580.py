import sys

input = sys.stdin.readline

def backtracking(depth):
    if depth == len(blanks):
        for row in matrix:
            print(*row, sep = ' ')

        exit()
    else:
        for i in range(1, 10):
            v = blanks[depth]

            if isPossiblePosition(v, i):
                matrix[v[0]][v[1]] = i
                backtracking(depth + 1)
                matrix[v[0]][v[1]] = 0

def isPossiblePosition(v, number):
    for i in range(9):
        if matrix[v[0]][i] == number or matrix[i][v[1]] == number:
            return False

    for i in range(3):
        for j in range(3):
            if matrix[(v[0] // 3) * 3 + i][(v[1] // 3) * 3 + j] == number:
                return False

    return True

matrix = [list(map(int, input().split())) for _ in range(9)]
blanks = [(row, column) for column in range(9) for row in range(9) if matrix[row][column] == 0]

backtracking(0)