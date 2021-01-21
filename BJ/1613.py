import sys

N, K = map(int, input().split(' '))
mat = [[sys.maxsize] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split(' '))
    mat[a-1][b-1] = 1
for i in range(N):
    mat[i][i] = 0

# 연결관계를 통해 전체 연결 관계를 알고 싶은 경우 -> 플로이드 와샬!
for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    ab, ba = mat[a-1][b-1], mat[b-1][a-1]

    if ab == sys.maxsize:
        if ba == sys.maxsize:
            print(0)
        else:
            print(1)
    else:
        print(-1)