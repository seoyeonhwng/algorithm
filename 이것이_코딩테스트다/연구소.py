from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

def bfs(mat, queue):
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] != 0:
                continue
            
            mat[nx][ny] = 2
            queue.append((nx, ny))

N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

empty, virus = [], deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            empty.append((i, j))
        elif mat[i][j] == 2:
            virus.append((i, j))

ans = -sys.maxsize
for a, b, c in combinations(empty, 3):
    new_mat = deepcopy(mat)
    new_mat[a[0]][a[1]] = 1
    new_mat[b[0]][b[1]] = 1
    new_mat[c[0]][c[1]] = 1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    bfs(new_mat, deepcopy(virus))

    count = 0
    for i in range(N):
        for j in range(M):
            if new_mat[i][j] == 0:
                count += 1
    ans = max(ans, count)

print(ans)