from copy import deepcopy

def move_up(x, y):
    # 오른쪽으로 쭉 이동
    val = 0
    while True:
        nx, ny = x, y + 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 위로 쭉 이동
    while True:
        nx, ny = x - 1, y
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 왼쪽으로 쭉 이동
    while True:
        nx, ny = x, y - 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 아래로 이동
    while True:
        nx, ny = x + 1, y
        if mat[nx][ny] == -1:
            break
        
        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

def move_down(x, y):
    # 오른쪽으로 쭉 이동
    val = 0
    while True:
        nx, ny = x, y + 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 아래로 쭉 이동
    while True:
        nx, ny = x + 1, y
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 왼쪽으로 쭉 이동
    while True:
        nx, ny = x, y - 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break

        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

    # 위로 이동
    while True:
        nx, ny = x - 1, y
        if mat[nx][ny] == -1:
            break
        
        tmp = mat[nx][ny]
        mat[nx][ny] = val
        x, y, val = nx, ny, tmp

R, C, T = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(T):
    # 미세먼지
    new_mat = deepcopy(mat)
    for x in range(R):
        for y in range(C):
            if mat[x][y] > 0: # 미세먼지 있음
                count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C or mat[nx][ny] == -1:
                        continue
                    
                    count += 1
                    new_mat[nx][ny] += mat[x][y] // 5
                new_mat[x][y] -= (mat[x][y] // 5) * count
    mat = new_mat

    count = 0
    for i in range(R):
        for j in range(C):
            if mat[i][j] == -1:
                if count == 0:
                    move_up(i, j)
                    count += 1
                else:
                    move_down(i, j)

answer = 0
for row in mat:
    answer += sum(r for r in row)
print(answer + 2)