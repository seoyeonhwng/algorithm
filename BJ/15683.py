import sys
from copy import deepcopy


def dfs(idx, check):
    global answer 
    # cctv 배열의 idx번째 cctv를 처리
    if idx == len(cctv):
        tmp = 0
        for r in check:
            tmp += sum(r)
        answer = min(answer, tmp)
        return

    num, x, y = cctv[idx]
    for di in direction[num]:
        tmp = deepcopy(check)
        for i in di:
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < N and 0 <= ny < M and mat[nx][ny] != 6:
                tmp[nx][ny] = 0
                nx, ny = nx + dx[i], ny + dy[i]
        
        dfs(idx + 1, tmp)


direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [0, 2], [3, 1], [2, 1]],
    [[0, 2, 3], [0, 3, 1], [2, 3, 1], [0, 1, 2]],
    [[0, 1, 2, 3]]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

check = [[1] * M for _ in range(N)]
cctv, cctv_count = [], 0
for i in range(N):
    for j in range(M):
        if mat[i][j] > 0:
            check[i][j] = 0
        if mat[i][j] >= 1 and mat[i][j] <= 5:
            cctv.append((mat[i][j], i, j))
            cctv_count += 1

answer = sys.maxsize
dfs(0, check)
print(answer)