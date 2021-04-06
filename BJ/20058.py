import sys
sys.setrecursionlimit(100000)

def rotate_mat(delta):
    for x in range(0, N, delta):
        for y in range(0, N, delta):

            tmp = [mat[i][y:y + delta] for i in range(x, x + delta)]
            for i in range(delta):
                for j in range(delta):
                    mat[x + j][y + delta - 1 - i] = tmp[i][j]

def dfs(x, y):
    rest = 1
    mat[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] > 0:
            rest += dfs(nx, ny)
    return rest


N, Q = map(int, input().split(' '))
N = 2 ** N
mat = [list(map(int, input().split(' '))) for _ in range(N)]
L = list(map(int, input().split(' ')))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for l in L:
    rotate_mat(2 ** l)

    count = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if mat[nx][ny] > 0:
                    count[x][y] += 1
    
    for i in range(N):
        for j in range(N):
            if mat[i][j] > 0 and count[i][j] < 3:
                mat[i][j] -= 1

print(sum(sum(r) for r in mat))

max_val = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            max_val = max(max_val, dfs(i, j))
print(max_val)
