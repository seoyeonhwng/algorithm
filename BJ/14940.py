from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(sx, sy, 0)])
    visited = [[-1] * M for _ in range(N)]
    visited[sx][sy] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == 0 or visited[nx][ny] != -1:
                continue
            queue.append((nx, ny, count + 1))
            visited[nx][ny] = count + 1
    return visited


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            sx, sy = i, j
            break

ans = bfs()
for i in range(N):
    for j in range(M):
        if ans[i][j] == -1 and mat[i][j] == 0:
            ans[i][j] = 0
for row in ans:
    print(*row)