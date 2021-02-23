import sys
sys.setrecursionlimit(10000000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] != '#':
        return
    
    mat[i][j] = '.'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1, j+1)
    dfs(i+1, j-1)
    dfs(i-1, j+1)
    dfs(i-1, j-1)


N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == '#':
            dfs(i, j)
            ans += 1
print(ans)