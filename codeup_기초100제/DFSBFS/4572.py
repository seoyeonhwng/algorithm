import sys
sys.setrecursionlimit(10000)

def dfs(mat, i, j):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return 0

    if mat[i][j] == 1:
        return 0
    
    mat[i][j] = 1
    return 1 + dfs(mat, i+1, j) + dfs(mat, i-1, j) + dfs(mat, i, j+1) + dfs(mat, i, j-1)

    
M, N, K = map(int, input().split(' '))
mat = [[0] * N for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split(' '))
    for i in range(b, d): # 색칠 -> mat를 뒤집지않아도 정답에는 영향을 주지않음!
        for j in range(a, c):
            mat[i][j] = 1

res, count = [], 0
for i in range(M):
    for j in range(N):
        if mat[i][j] == 0:
            res.append(dfs(mat, i, j))
            count += 1

print(count)
print(' '.join(map(str, sorted(res))))

"""
* DFS에서 섬의 넓이가 필요하거나 path의 길이만 필요한 경우 지금처럼 1 + 상하좌우를 return 한다!!!!
"""