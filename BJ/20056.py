from copy import deepcopy

def check_direction(mat):
    tmp = [e[2] % 2 for e in mat]
    length = len(mat)
    return sum(tmp) == 0 or sum(tmp) == length

N, M, K = map(int, input().split(' '))
mat = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split(' '))
    mat[r-1][c-1].append((m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 모든 파이어볼 자신의 방향 di로 속력 si칸 만큼 이동한다.
for _ in range(K):
    new_mat = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for m, s, d in mat[x][y]:
                nx, ny = (x + s * dx[d]) % N, (y + s * dy[d]) % N
                new_mat[nx][ny].append((m, s, d))

    for x in range(N):
        for y in range(N):
            count = len(new_mat[x][y])
            if count >= 2:
                new_m = sum([e[0] for e in new_mat[x][y]]) // 5
                if new_m == 0:
                    new_mat[x][y] = []
                    continue

                new_s = sum([e[1] for e in new_mat[x][y]]) // count
                direction = [0, 2, 4, 6] if check_direction(new_mat[x][y]) else [1, 3, 5, 7]

                new_ball = []
                for d in direction:
                    new_ball.append((new_m, new_s, d))
                new_mat[x][y] = new_ball
    mat = new_mat

answer = 0
for i in range(N):
    for j in range(N):
        for m, _, _ in mat[i][j]:
            answer += m
print(answer)
