import sys
sys.setrecursionlimit(1000000)

def dfs(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    if mat[i][j] == '.':
        return

    mat[i][j] = '.'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

for _ in range(int(input())):
    H, W = map(int, input().split(' '))
    mat = [list(input()) for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if mat[i][j] == '#':
                dfs(i, j)
                ans += 1
    print(ans)
