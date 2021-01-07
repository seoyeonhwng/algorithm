import sys
sys.setrecursionlimit(10000)

def fill(a, b, c, d):
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b

    for i in range(b, d):
        for j in range(a, c):
            mat[i][j] = 1

def dfs(i, j):
    if i < 0 or i >= M or j < 0 or j >= N:
        return
    if mat[i][j] == 1:
        return
    
    path.append((i, j))
    mat[i][j] = 1
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


M, N, K = map(int, input().split(' '))
mat = [[0] * N for _ in range(M)]
for _ in range(K):
    a, b, c, d = map(int, input().split(' '))
    fill(a, b, c, d)

result = []
for i in range(M):
    for j in range(N):
        if mat[i][j] == 0:
            path = []
            dfs(i, j)
            result.append(len(path))
        
result.sort()
print(len(result))
print(*result)