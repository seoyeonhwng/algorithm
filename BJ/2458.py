import sys

N, M = map(int, input().split(' '))
mat = [[sys.maxsize] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    mat[a-1][b-1] = 1

# 플로이드-와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][k] + mat[k][j] == 2: # 갈수있다면 1로 표시
                mat[i][j] = 1

count = [0] * N
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            count[i] += 1
            count[j] += 1

print(count.count(N-1))