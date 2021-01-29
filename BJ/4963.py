import sys
sys.setrecursionlimit(1000000)

def dfs(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    if maps[i][j] == 0:
        return
    
    maps[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i+1, j+1)
    dfs(i+1, j-1)
    dfs(i-1, j+1)
    dfs(i-1, j-1)

while True:
    W, H = map(int, input().split(' '))
    if W == 0 and H == 0:
        break

    maps = [list(map(int, input().split(' '))) for _ in range(H)]

    count = 0
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)