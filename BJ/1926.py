import sys
sys.setrecursionlimit(10000000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] == 0:
        return

    path.append((i, j))
    mat[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

input = sys.stdin.readline
N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

total, area = 0, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            path = []
            dfs(i, j)
            total += 1
            area = max(area, len(path))

print(total)
print(area)