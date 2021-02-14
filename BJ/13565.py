import sys
sys.setrecursionlimit(10000000)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if mat[x][y] != 0:
        return

    mat[x][y] = 2
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

M, N = map(int, input().split(' '))
mat = [list(map(int, list(input()))) for _ in range(M)]

# 첫번째 행에 0이면 list에 넣어
# 그 애들로 dfs
# 마지막에 맨 아래 행까지 왔는지 체크

start = []
for i in range(N):
    if mat[0][i] == 0:
        start.append((0, i))

for sx, sy in start:
    dfs(sx, sy)

ans = 'NO'
for i in range(N):
    if mat[M-1][i] == 2:
        ans = 'YES'
print(ans)