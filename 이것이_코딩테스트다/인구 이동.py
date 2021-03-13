from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy):
    queue = deque([(sx, sy, mat[sx][sy])])
    path = set([(sx, sy)])
    total = mat[sx][sy]

    while queue:
        x, y, val = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in path:
                continue
            
            diff = abs(val - mat[nx][ny])
            if L <= diff <= R:
                path.add((nx, ny))
                total += mat[nx][ny]
                queue.append((nx, ny, mat[nx][ny]))

    return path, total

def move(info):
    for path, val in info:
        val = val // len(path)
        for x, y in path:
            mat[x][y] = val


N, L, R = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0
while True:
    move_info = []
    for i in range(N):
        for j in range(N):
            path, val = bfs(i, j)
            if val > mat[i][j]:
                move_info.append((path, val))

    if not move_info:
        break

    ans += 1
    move(move_info)
print(ans)