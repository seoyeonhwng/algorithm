import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] == 0:
        return
    
    path.append((i, j))
    mat[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i,  j-1)

N, M, K = map(int, input().split(' '))

mat = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split(' '))
    mat[r-1][c-1] = 1

ans = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            path = []
            dfs(i, j)
            ans = max(ans, len(path))
print(ans)