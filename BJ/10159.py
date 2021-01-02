import sys

N = int(input())
M = int(input())
mat = [[sys.maxsize] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    mat[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][k] + mat[k][j] == 2:
                mat[i][j] = 1

check = [0] * N
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            check[i] += 1
            check[j] += 1

for c in check:
    print(N - c - 1)


