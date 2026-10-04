import sys

data = list(map(int, sys.stdin.read().split()))

# First two values are rows and columns
n = data[0]
m = data[1]

grid = []
idx = 2

for i in range(n):
    grid.append(data[idx:idx + m])
    idx += m

# dp[i][j] = minimum cost to reach (i, j)
dp = [[0] * m for _ in range(n)]

dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        best = float('inf')

        # From top
        if i > 0:
            best = min(best, dp[i - 1][j])

        # From left
        if j > 0:
            best = min(best, dp[i][j - 1])

        # From diagonal
        if i > 0 and j > 0:
            best = min(best, dp[i - 1][j - 1])

        dp[i][j] = grid[i][j] + best

print(dp[n - 1][m - 1])
