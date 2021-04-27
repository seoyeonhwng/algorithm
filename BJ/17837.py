from collections import defaultdict
from copy import deepcopy

def get_pos(idx):
    for i in range(N):
        for j in range(N):
            if idx in mat[i][j]:
                return (i, j)

def get_opposite_d(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3

def move_white(num, x, y, nx, ny):
    # x,y에 있는 idx말이 nx,ny로 이동
    # 이동할때는 idx보다 위에 있는 말은 같이 이동
    # nx,ny에 append
    idx = mat[x][y].index(num)
    horses = deepcopy(mat[x][y][idx:])
    mat[x][y] = deepcopy(mat[x][y][:idx])
    mat[nx][ny] += horses

def move_red(num, x, y, nx, ny):
    idx = mat[x][y].index(num)
    horses = deepcopy(mat[x][y][idx:])
    mat[x][y] = deepcopy(mat[x][y][:idx])

    horses.reverse()
    mat[nx][ny] += horses

def move(idx):
    # idx번째 말을 이동시키고 만약 4개 이상 있다면 True를 리턴
    x, y = get_pos(idx)
    d = direction[idx]

    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or color[nx][ny] == 2:
        # 방향을 바꿔서 새로운 nx, ny를 구함
        nd = get_opposite_d(d)
        direction[idx] = nd
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < N and color[nx][ny] == 0:
            move_white(idx, x, y, nx, ny)
        if 0 <= nx < N and 0 <= ny < N and color[nx][ny] == 1:
            move_red(idx, x, y, nx, ny)
    elif 0 <= nx < N and 0 <= ny < N and color[nx][ny] == 0:
        move_white(idx, x, y, nx, ny)
    elif 0 <= nx < N and 0 <= ny < N and color[nx][ny] == 1:
        move_red(idx, x, y, nx, ny)

    for i in range(N):
        for j in range(N):
            if len(mat[i][j]) >= 4:
                return True
    return False

def play():
    for i in range(1, K+1):
        if move(i):
            return True
    return False


N, K = map(int, input().split(' '))
color = [list(map(int, input().split(' '))) for _ in range(N)]

mat = [[[] for _ in range(N)] for _ in range(N)]
direction = defaultdict(int)
for i in range(1, K+1):
    x, y, d = map(int, input().split(' '))
    mat[x-1][y-1].append(i)
    direction[i] = d

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

answer = 1
while True:
    result = play()
    if result or answer > 1000:
        break

    answer += 1
print(-1) if answer > 1000 else print(answer)

# 방향이 있으면 방향을 따로 관리!!
# 함수 단위로 먼저 짠다!!