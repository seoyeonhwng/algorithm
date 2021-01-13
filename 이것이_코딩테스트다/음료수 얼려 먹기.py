def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] == 1:
        return
    
    mat[i][j] = 1 # 방문 표시
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

N, M = map(int, input().split(' '))
mat = [list(map(int, input())) for _ in range(N)]

# DFS 몇번 할 수 있는가
count = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)