
def dfs(i, j):
    if i < 0 or i >= R or j < 0 or j >= C:
        return
    if maps[i][j] == '.':
        return
    
    maps[i][j] = '.'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

R, C = map(int, input().split(' '))
maps = [list(input()) for _ in range(R)]

ans = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] == '#':
            dfs(i, j)
            ans += 1
print(ans)