import sys
sys.setrecursionlimit(10000000)

def dfs(x, y, v):
    if x < 0 or x >= R or y < 0 or y >= C:
        return
    if mat[x][y] != v:
        return
    
    mat[x][y] = color
    dfs(x+1, y, v)
    dfs(x-1, y, v)
    dfs(x, y+1, v)
    dfs(x, y-1, v)

R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]
sx, sy, color = map(int, input().split(' '))

dfs(sx, sy, mat[sx][sy])

for row in mat:
    print(''.join([str(r) for r in row]))