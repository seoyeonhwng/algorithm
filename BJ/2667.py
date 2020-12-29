def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if mat[i][j] == 0:
        return
    
    path.append((i, j))
    mat[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int, input())))

result = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            path = []
            dfs(i, j)
            result.append(len(path))

print(len(result))
print(*sorted(result), sep='\n')