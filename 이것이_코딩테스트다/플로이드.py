import sys
input = sys.stdin.readline

N = int(input())
mat = [[sys.maxsize] * N for _ in range(N)]

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    mat[a-1][b-1] = min(mat[a-1][b-1], c)

for i in range(N):
    mat[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

for i in range(N):
    for j in range(N):
        if mat[i][j] == sys.maxsize:
            mat[i][j] = 0
for row in mat:
    print(*row)