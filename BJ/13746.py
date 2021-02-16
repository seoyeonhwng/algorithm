def dfs(i, j):
    if i < 0 or i >= R or j < 0 or j >= C:
        return
    if mat[i][j] == 'W':
        return
    
    mat[i][j] = 'W'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]

ans = 0
for i in range(R):
    for j in range(C):
        if mat[i][j] == 'L':
            dfs(i, j)
            ans += 1
print(ans)