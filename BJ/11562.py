import sys

N, M = map(int, input().split(' '))

mat = [[sys.maxsize] * N for _ in range(N)]

# 양방향 도로의 개수를 기준으로 그래프를 정의!
for _ in range(M):
    u, v, b = map(int, input().split(' '))
    mat[u-1][v-1] = 0
    mat[v-1][u-1] = 1 if b == 0 else 0 # 단방향인 경우, v에서 u까지 가려면 양방향 도로를 둬야하므로 비용이 1
for i in range(N):
    mat[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in  range(N):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

for _ in range(int(input())):
    s, e = map(int, input().split(' '))
    print(mat[s-1][e-1])