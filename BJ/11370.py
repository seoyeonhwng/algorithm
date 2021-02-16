def dfs(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    if mat[i][j] != 'T':
        return 

    mat[i][j] = 'S'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

while True:
    W, H = map(int, input().split(' '))
    if W == 0 and H == 0:
        break
    mat = [list(input()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if mat[i][j] == 'S':
                mat[i][j] = 'T'
                dfs(i, j)
                mat[i][j] = 'S'
    for r in mat:
        print(''.join(r))