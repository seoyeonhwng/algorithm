from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

def dfs(i, j, v):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if maps[i][j] != v:
        return

    maps[i][j] = '#'
    dfs(i+1, j, v)
    dfs(i-1, j, v)
    dfs(i, j+1, v)
    dfs(i, j-1, v)


N = int(input())
mat = [list(input()) for _ in range(N)]
ans = []

# 적록색약이 아닌 사람이 봤을때
maps, count = deepcopy(mat), 0
for i in range(N):
    for j in range(N):
        if maps[i][j] != '#':
            dfs(i, j, maps[i][j])
            count += 1
ans.append(count)

# 적록색약인 사람이 봤을때
maps, count = deepcopy(mat), 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == 'R':
            maps[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if maps[i][j] != '#':
            dfs(i, j, maps[i][j])
            count += 1
ans.append(count)

print(*ans)