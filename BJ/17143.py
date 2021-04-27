from copy import deepcopy

def eat_shark(col): # 해당 열에서 땅이랑 가장 가까운 상어 먹기
    for i in range(R):
        if mat[i][col]:
            n = mat[i][col][0]
            mat[i][col] = []
            return sharks[n][2]
    return 0

def get_opposite_d(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3

def move_shark(x, y, num):
    # mat[x][y]에 위치하고 있는 num번째 상어 이동
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]

    s, d, z = sharks[num]
    
    count = 0
    while count < s:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d = get_opposite_d(d)
            sharks[num] = (s, d, z)
        else:
            x, y = nx, ny
            count += 1

    return x, y

def move():
    new_mat = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if mat[i][j] == []:
                continue

            num = mat[i][j][0]
            nx, ny = move_shark(i, j, num)
            new_mat[nx][ny].append(num)

    return new_mat

def check(mat):
    for i in range(R):
        for j in range(C):
            if len(mat[i][j]) <= 1:
                continue
                
            big_num, big_size = mat[i][j][0], sharks[mat[i][j][0]][2]
            for n in mat[i][j]:
                if sharks[n][2] > big_size:
                    big_num, big_size = n, sharks[n][2]
            
            mat[i][j] = [big_num]
    return mat



R, C, M = map(int, input().split(' '))
mat = [[[] for _ in range(C)] for _ in range(R)]

sharks = {}
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split(' '))
    mat[r-1][c-1].append(i)
    sharks[i] = (s, d, z)


answer = 0
for col in range(C):
    # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    answer += eat_shark(col)
    # 상어가 이동한다.
    new_mat = move()

    # 한 칸에 여러마리 있는지 체크
    mat = check(new_mat)
print(answer)