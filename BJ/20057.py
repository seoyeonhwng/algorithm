from copy import deepcopy

def get_info(d):
    if d == 0:
        dx = [1, -1, 2, -2, -1, 1, 0, -1, 1, 0]
        dy = [0, 0, 0, 0, 1, 1, -1, -1, -1, -2]
        r = [0.07, 0.07, 0.02, 0.02, 0.01, 0.01, 'a', 0.1, 0.1, 0.05]
    elif d == 1:
        dx = [0, 0, 0, 0, 1, 1, 1, 2, -1, -1]
        dy = [1, -1, 2, -2, 1, -1, 0, 0, 1, -1]
        r = [0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 'a', 0.05, 0.01, 0.01]
    elif d == 2:
        dx = [1, -1, 2, -2, 1, -1, 0, 0, 1, -1]
        dy = [0, 0, 0, 0, 1, 1, 1, 2, -1, -1]
        r = [0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 'a', 0.05, 0.01, 0.01]
    elif d == 3:
        dx = [0, 0, 0, 0, -1, -1, -1, -2, 1, 1]
        dy = [1, -1, 2, -2, 1, -1, 0, 0, 1, -1]
        r = [0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 'a', 0.05, 0.01, 0.01]
    return dx, dy, r

def move(x, y, d):
    dx, dy, r = get_info(d)

    out, res = 0, mat[x][y]
    for i in range(10):
        nx, ny = x + dx[i], y + dy[i]
        if r[i] == 'a':
            ax, ay = nx, ny
            continue
        
        res -= int(mat[x][y] * r[i])
        if nx < 0 or nx >= N or ny < 0 or ny >= N: # 격자 밖 모래
            out += int(mat[x][y] * r[i])
        else:
            mat[nx][ny] += int(mat[x][y] * r[i])
    
    # res = alpha
    if ax < 0 or ax >= N or ay < 0 or ay >= N:
        out += res
    else:
        mat[ax][ay] += res

    mat[x][y] = 0
    return out


N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]

op, d = [], 0
for i in range(1, N):
    for _ in range(2):
        op.append([i, d])
        d = (d + 1) % 4
op.append([N-1, d])

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x, y = N // 2, N // 2

ans = 0
for count, d in op:
    # 모래를 d방향으로 count만큼 이동
    for _ in range(count):
        x, y = x + dx[d], y + dy[d]
        ans += move(x, y, d)
print(ans)