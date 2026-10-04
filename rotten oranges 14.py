import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque()
fresh = 0

# Add all rotten oranges to the queue
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            q.append((i, j))
        elif grid[i][j] == 1:
            fresh += 1

# No fresh oranges
if fresh == 0:
    print(0)
    sys.exit()

time = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    # Process all oranges that rot at the current time
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc))

    if q:
        time += 1

if fresh == 0:
    print(time)
else:
    print(-1)
