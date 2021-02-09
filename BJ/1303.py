def dfs(i, j, c):
    if i < 0 or i >= M or j < 0 or j >= N:
        return
    if mat[i][j] != c:
        return
    
    path.append((i, j))
    mat[i][j] = '.'
    dfs(i+1, j, c)
    dfs(i-1, j, c)
    dfs(i, j+1, c)
    dfs(i, j-1, c)
    

N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(M)]

white, black = 0, 0
for i in range(M):
    for j in range(N):
        if mat[i][j] == 'W' or mat[i][j] == 'B':
            c = mat[i][j]
            path = []
            dfs(i, j, c)
            if c == 'W':
                white += len(path) ** 2
            else:
                black += len(path) ** 2
print(f'{white} {black}')