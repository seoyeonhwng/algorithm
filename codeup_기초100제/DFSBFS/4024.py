import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    if area[i][j] == '.':
        return

    area[i][j] = '.'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

    dfs(i+1, j+1)
    dfs(i-1, j+1)
    dfs(i+1, j-1)
    dfs(i-1, j-1)


W, H = map(int, input().split(' '))
area = [input().split(' ') for _ in range(H)]

count = 0
for i in range(H):
    for j in range(W):
        if area[i][j] == 'L':
            dfs(i, j)
            count += 1

print(count)