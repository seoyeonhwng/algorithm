def move1(x, y):
    # 오른쪽으로 이동해서 파란색
    x1, y1 = x, y
    while True:
        nx, ny = x1, y1 + 1
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x1, y1 = nx, ny
    mat[x1][y1] = 1

    # 아래로 이동해서 빨간색
    x2, y2 = x, y
    while True:
        nx, ny = x2 + 1, y2
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x2, y2 = nx, ny
    mat[x2][y2] = 1

def move2(x, y):
    # 오른쪽으로 쭉 이동 -> (x, y+1)을 최대한 이동시키고 위치 + (x,y)를 위치
    x1, y1 = x, y + 1
    while True:
        nx, ny = x1, y1 + 1
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x1, y1 = nx, ny
    mat[x1][y1] = 1
    mat[x1][y1-1] = 1

    # 아래로 쭉 이동
    x2, y2 = x, y
    while True:
        nx, ny = x2 + 1, y2
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x2, y2 = nx, ny
    
    x3, y3 = x, y + 1
    while True:
        nx, ny = x3 + 1, y3
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x3, y3 = nx, ny
    
    new_x = min(x2, x3)
    mat[new_x][y] = 1
    mat[new_x][y+1] = 1

def move3(x, y):
    # 아래로 쭉 이동 -> (x+1, y)를 최대한 이동시키고 위치 + (x, y)도 위치
    x1, y1 = x + 1, y
    while True:
        nx, ny = x1 + 1, y1
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x1, y1 = nx, ny
    mat[x1][y1] = 1
    mat[x1-1][y1] = 1

    # 오른쪽으로 쭉 둘 다 이동 -> y 최소!
    x2, y2 = x, y
    while True:
        nx, ny = x2, y2 + 1
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x2, y2 = nx, ny
    
    x3, y3 = x + 1, y
    while True:
        nx, ny = x3, y3 + 1
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or mat[nx][ny] == 1:
            break
        x3, y3 = nx, ny
    
    new_y = min(y2, y3)
    mat[x][new_y] = 1
    mat[x+1][new_y] = 1

def move_down(idx):
    for i in range(idx-1, -1, -1):
        for j in range(4):
            mat[i+1][j] = mat[i][j]

def move_down2(idx):
    for i in range(8, idx-2, -1):
        for j in range(4):
            mat[i+1][j] = mat[i][j]

def check_green2():
    tmp = [False] * 2
    for i in range(4, 6):
        for j in range(4):
            if mat[i][j] == 1:
                tmp[i-4] = True
    
    for i in range(2):
        if tmp[i]:
            move_down2(i+4)

def check_green(answer):
    for i in range(6, 10):
        count = 0
        for j in range(4):
            count += mat[i][j]
        
        if count == 4:
            move_down(i)
            answer += 1
    return answer

def move_right(idx):
    for i in range(4):
        for j in range(idx-1, -1, -1):
            mat[i][j+1] = mat[i][j]

def move_right2(idx):
    for i in range(4):
        for j in range(8, idx-2, -1):
            mat[i][j+1] = mat[i][j]

def check_blue2():
    tmp = [False] * 2
    for j in range(4, 6):
        for i in range(4):
            if mat[i][j] == 1:
                tmp[j-4] = True
    
    for i in range(2):
        if tmp[i]:
            move_right2(i+4)

def check_blue(answer):
    for j in range(6, 10):
        count = 0
        for i in range(4):
            count += mat[i][j]
        
        if count == 4:
            move_right(j)
            answer += 1
    return answer

mat = [[0] * 10 for _ in range(10)]
answer = 0
for _ in range(int(input())):
    t, x, y = map(int, input().split(' '))
    if t == 1:
        move1(x, y)
    elif t == 2:
        move2(x, y)
    else:
        move3(x, y)
    
    answer = check_green(answer)
    answer = check_blue(answer)

    check_blue2()
    check_green2()

print(answer)
total = 0
for i in range(6, 10):
    for j in range(4):
        total += mat[i][j]
for i in range(4):
    for j in range(6, 10):
        total += mat[i][j]
print(total)