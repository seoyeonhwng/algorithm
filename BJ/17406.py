from itertools import permutations
import sys
from copy import deepcopy

def do_rotation(r, c, s):
    for i in range(1, s+1):
        x, y = r - i, c - i
        prev = mat[x][y]
        for d in range(4):
            for _ in range(2*i):
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                tmp = mat[nx][ny]
                mat[nx][ny] = prev
                prev = tmp
                x, y = nx, ny


N, M, K = map(int, input().split(' '))
origin_mat = [list(map(int, input().split(' '))) for _ in range(N)]
op = []
for _ in range(K):
    r, c, s = map(int, input().split(' '))
    op.append((r-1, c-1, s))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = sys.maxsize
for candi in permutations(op):
    mat = deepcopy(origin_mat)
    for r, c, s in candi:
        do_rotation(r, c, s)
    
    total = sys.maxsize
    for row in mat:
        total = min(total, sum(row))
    
    answer = min(answer, total)
print(answer)