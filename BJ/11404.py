import sys

N = int(input())
M = int(input())

matrix = [[sys.maxsize] * N for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split(' '))
    matrix[a-1][b-1] = min(matrix[a-1][b-1], w)

for i in range(N):
    matrix[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == sys.maxsize:
            matrix[i][j] = 0
            
for row in matrix:
    print(' '.join(str(r) for r in row))