from collections import deque
import sys
input = sys.stdin.readline

def dfs():
    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    while queue:
        x, y, count = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == -1:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = count + 1



N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# 1인 곳 다 넣고 bfs!!
queue = deque()
visited = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            queue.append((i, j, 0))
            visited[i][j] = 0

dfs()
ans = -sys.maxsize
for row in visited:
    ans = max(ans, max(row))
print(ans)

