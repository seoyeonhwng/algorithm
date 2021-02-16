import sys
sys.setrecursionlimit(10000000)

def dfs(i, j):
    if i < 0 or i >= M or j < 0 or j >= N:
        return
    if mat[i][j] != 1:
        return

    mat[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1, j-1)
    dfs(i+1, j+1)
    dfs(i-1, j+1)
    dfs(i-1, j-1)

M, N = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(M)]

ans = 0
for i in range(M):
    for j in range(N):
        if mat[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)