def dfs(i, j, v):
    if i < 0 or i >= 12 or j < 0 or j >= 6:
        return
    if mat[i][j] != v or (i, j) in path:
        return

    visited[i][j] = True
    path.append((i, j))
    dfs(i+1, j, v)
    dfs(i-1, j, v)
    dfs(i, j+1, v)
    dfs(i, j-1, v)

def delete(nodes):
    for x, y in nodes:
        mat[x][y] = '.'

def move(i, j):
    while i-1 >= 0 and mat[i-1][j] != '.':
        mat[i][j], mat[i-1][j] = mat[i-1][j], mat[i][j]
        i -= 1

mat, ans = [list(input()) for _ in range(12)], 0
while True:
    # 상하좌우 4개 이상 골라서 제거
    visited, count = [[False] * 6 for _ in range(12)], 0
    for i in range(12):
        for j in range(6):
            if mat[i][j] != '.' and not visited[i][j]:
                path = []
                dfs(i, j, mat[i][j])
                if len(path) >= 4:
                    delete(path)
                    count += 1
    
    # 더이상 터질게 없는 경우
    if count == 0:
        print(ans)
        break
    
    # 밑으로 이동
    for i in range(12):
        for j in range(6):
            if mat[i][j] == '.' and i-1 >= 0 and mat[i-1][j] != '.':
                move(i, j)
    
    ans += 1