import sys

input = sys.stdin.readline

def dfs(v):
    visited[v[0]][v[1]] = True

    if v == (n - 1, n - 1):
        return 1
    elif dp[v[0]][v[1]] > -1:
        return dp[v[0]][v[1]]
    else:
        dp[v[0]][v[1]] = 0

        for next_v in ((v[0] + matrix[v[0]][v[1]], v[1]), (v[0], v[1] + matrix[v[0]][v[1]])):
            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                dp[v[0]][v[1]] += dfs(next_v)
                visited[next_v[0]][next_v[1]] = False

    return dp[v[0]][v[1]]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dfs((0, 0))

print(dp[0][0])