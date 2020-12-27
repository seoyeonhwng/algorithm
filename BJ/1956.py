import sys

V, E = map(int, input().split(' '))

mat = [[sys.maxsize] * V for _ in range(V)]
for _ in range(E):
    a, b, w = map(int, input().split(' '))
    mat[a-1][b-1] = w

# 플로이드 와샬로 그래프에 사이클이 하나라도 존재하는지 체크 가능
for k in range(V):
    for i in range(V):
        for j in range(V):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[i][k] + mat[k][j]

answer = sys.maxsize
for i in range(V):
    answer = min(answer, mat[i][i])
print(answer) if answer != sys.maxsize else print(-1)