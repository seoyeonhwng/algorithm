def dfs(i, j):
    if i < 0 or i >= 10 or j < 0 or j >= 10:
        return
    if area[i][j] == '*':
        return
    
    area[i][j] = '*'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i, j+1)

area = [list(input()) for _ in range(10)]
x, y = map(int, input().split(' '))

dfs(y, x)
for a in area:
    print(''.join(a))