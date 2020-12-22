import sys

N, M = map(int, input().split(' '))
matrix = [[sys.maxsize] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for i in range(N):
    matrix[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = {}
for i, row in enumerate(matrix):
    answer[i] = sum(row)

answer = sorted(answer.items(), key=lambda x: (x[1], x[0]))
print(answer[0][0] + 1)
