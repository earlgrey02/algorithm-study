import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v):
    visited[v[0]][v[1]] = True

    if dp[v[0]][v[1]] >= 0:
        return dp[v[0]][v[1]]
    else:
        dp[v[0]][v[1]] = matrix[v[0]][v[1]]

        for i in range(3):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                dp[v[0]][v[1]] = max(dp[v[0]][v[1]], matrix[v[0]][v[1]] + dfs(next_v))
                visited[next_v[0]][next_v[1]] = False

    return dp[v[0]][v[1]]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dy = (1, 0, 1)
dx = (0, 1, 1)

dfs((0, 0))

print(max(map(max, dp)))