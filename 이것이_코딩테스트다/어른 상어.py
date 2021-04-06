from collections import deque, defaultdict

def get_next_pos(x, y): # 다음 이동 방향을 정해서 결정
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    s_num, d, _ = mat[x][y]

    for i in priority[s_num][d]:
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if mat[nx][ny] == []:
            return nx, ny, i

    for i in priority[s_num][d]:
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if mat[nx][ny][0] == s_num:
            return nx, ny, i

def move_shark():
    candi = defaultdict(list)

    for x in range(N):
        for y in range(N):
            if mat[x][y] == []:
                continue

            s_num, s_d, k = mat[x][y]
            if (s_num not in out) and (s_d != 0):
                # 다음 이동 방향을 정해서 이동
                nx, ny, nd = get_next_pos(x, y)
                candi[(nx, ny)].append([s_num, nd])
                mat[x][y] = [s_num, 0, k]

    return candi



N, M, K = map(int, input().split(' '))
tmp = [list(map(int, input().split(' '))) for _ in range(N)]
s_direction = list(map(int, input().split(' ')))

priority = [[0] * 5 for _ in range(M + 1)]
for i in range(1, M+1):
    for j in range(1, 5):
        priority[i][j] = list(map(int, input().split(' ')))

mat = [[[]] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if tmp[i][j] > 0:
            s_num = tmp[i][j]
            mat[i][j] = [s_num, s_direction[s_num-1], K]

target, out = set([i for i in range(1, M+1)]), set()
ans = 0

while True:
    ans += 1

    candi = move_shark()
    for key, values in candi.items():
        if len(values) == 1:
            mat[key[0]][key[1]] = [values[0][0], values[0][1], K]
        else:
            values.sort()
            mat[key[0]][key[1]] = [values[0][0], values[0][1], K]
            
            length = len(values)
            for i in range(1, length):
                out.add(values[i][0])

    for i in range(N):
        for j in range(N):
            if mat[i][j] == [] or mat[i][j][1] != 0:
                continue

            s_num, s_d, k = mat[i][j]
            if k == 1:
                mat[i][j] = []
            else:
                mat[i][j] = [s_num, s_d, k - 1]

    if target - out == {1} or ans > 1000:
        break
print(-1) if ans > 1000 else print(ans)
