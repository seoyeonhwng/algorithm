import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] == 0:
        return

    mat[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split(' '))
    mat = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split(' '))
        mat[b][a] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)