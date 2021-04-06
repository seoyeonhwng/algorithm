from collections import deque
from copy import deepcopy

def get_pos(mat, n):
    for i in range(4):
        for j in range(4):
            if mat[i][j][0] == n:
                return (i, j, mat[i][j][1])

def move_fish(mat, sx, sy):
    for n in range(1, 17):
        result = get_pos(mat, n)
        if not result:
            continue
 
        x, y, d = result
        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx, ny) == (sx, sy):
                d = (d + 1) % 8
                continue
            
            mat[x][y][1] = d
            mat[x][y], mat[nx][ny] = mat[nx][ny], mat[x][y]
            break

def move_shark(mat, sx, sy):
    x, y, d = sx, sy, mat[sx][sy][1]
    poss = []

    for _ in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or mat[nx][ny][0] == -1:
            x, y = nx, ny
            continue

        poss.append((nx, ny))
        x, y = nx, ny
    return poss

            
mat = [[0] * 4 for _ in range(4)]
for i in range(4):
    tmp = deque(list(map(int, input().split(' '))))
    for j in range(4):
        v, d = tmp.popleft(), tmp.popleft()
        mat[i][j] = [v, d-1]

# 물고기 이동
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
def dfs(maps, x, y, total):
    # (x, y)좌표에 있는 물고기 먹고
    # 물고기 전체 이동
    # 상어가 움직일 수 있는 모든 좌표에 대해 dfs 호출
    global ans

    maps = deepcopy(maps)
    total += maps[x][y][0]
    maps[x][y][0] = -1 # 해당 물고기 먹음

    move_fish(maps, x, y)
    poss = move_shark(maps, x, y)
    if len(poss) == 0:
        ans = max(ans, total)
        return

    for nx, ny in poss:
        dfs(maps, nx, ny, total)

dfs(mat, 0, 0, 0)
print(ans)