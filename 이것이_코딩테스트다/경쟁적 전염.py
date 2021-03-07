import sys
from collections import deque

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, k, count = queue.popleft()
        if count == S:
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if count < S and virus[nx][ny] == sys.maxsize:
                queue.append((nx, ny, k, count + 1))
                virus[nx][ny] = k




N, K = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]
S, X, Y = map(int, input().split(' '))

virus = [[sys.maxsize] * N for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(N):
        if mat[i][j] != 0:
            virus[i][j] = mat[i][j]
            queue.append((i, j, mat[i][j], 0))

# 낮은 번호부터 증식하므로 초기에 큐에 낮은 번호부터 삽입해야함
queue = deque(sorted(queue, key=lambda x:x[2]))
bfs()
print(0) if virus[X-1][Y-1] == sys.maxsize else print(virus[X-1][Y-1])