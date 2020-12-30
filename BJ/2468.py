from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if maps[i][j] <= depth:
        return
    
    maps[i][j] = depth
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i, j+1)


N = int(input())
matrix, max_depth = [], 0

for _ in range(N):
    row = list(map(int, input().split(' ')))
    matrix.append(row)
    max_depth = max(max_depth, max(row))

answer = 1
for depth in range(1, max_depth+1):
    maps, count = deepcopy(matrix), 0

    # depth이하는 갈수없음
    for i in range(N):
        for j in range(N):
            if maps[i][j] > depth:
                dfs(i, j)
                count += 1
    answer = max(answer, count)

print(answer)
