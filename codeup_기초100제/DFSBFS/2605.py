def dfs(mat, i, j, target, path):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return
    if mat[i][j] != target or (i, j) in path:
        return

    path.append((i, j))
    dfs(mat, i+1, j, target, path)
    dfs(mat, i-1, j, target, path)
    dfs(mat, i, j-1, target, path)
    dfs(mat, i, j+1, target, path)


mat = []
for i in range(7):
    mat.append(list(input().replace(' ', '')))

answer = set()
for i in range(7):
    for j in range(7):
        path = []
        dfs(mat, i, j, mat[i][j], path)
        path = tuple(sorted(path))
        if len(path) >= 3 and (path not in answer):
            answer.add(path)

print(len(answer))