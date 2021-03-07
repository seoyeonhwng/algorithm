from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 초원이면 그냥 감
            if mat[nx][ny] == '.' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
            else:
                # 빙판 또는 산 -> 초원 만날때까지 이동
                while 0 <= nx < N and 0 <= ny < M and mat[nx][ny] != '.':
                    if mat[nx][ny] == '#':
                        nx, ny = nx - dx[i], ny - dy[i]
                        break
                    nx, ny = nx + dx[i], ny + dy[i]
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
           

N, M = map(int, input().rstrip().split(' '))
mat = [list(input().rstrip()) for _ in range(N)]

queue = deque()
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if mat[i][j] == 'W':
            queue.append((i, j))
            visited[i][j] = True

bfs()
for i in range(N):
    for j in range(M):
        if mat[i][j] == '.' and not visited[i][j]:
            mat[i][j] = 'P'

for row in mat:
    print(''.join([r for r in row]))