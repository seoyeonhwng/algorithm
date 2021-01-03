from collections import defaultdict, deque

"""
# 내 풀이
import sys
from copy import deepcopy
sys.setrecursionlimit(100000)

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    if mat[i][j] == 0 or (i, j) in path:
        return

    path.add((i, j))
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

def get_zero_count(i, j):
    count = 0
    if matrix[i+1][j] == 0:
        count += 1
    if matrix[i-1][j] == 0:
        count += 1
    if matrix[i][j+1] == 0:
        count += 1
    if matrix[i][j-1] == 0:
        count += 1
    return count

N, M = map(int, input().split(' '))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(' '))))

days = 0
while True:
    days += 1
    mat = deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                mat[i][j] -= get_zero_count(i, j)
                if mat[i][j] < 0:
                    mat[i][j] = 0

    count, path = 0, set()
    for i in range(N):
        for j in range(M):
            if mat[i][j] > 0 and (i, j) not in path:
                dfs(i, j)
                count += 1

    if count >= 2:
        print(days)
        break
    if count == 0:
        print(0)
        break
    matrix = mat
"""
# 좋은 풀이
# 나는 빙하를 녹이고나서 dfs로 땅의 개수를 셌는데 bfs로 땅의 개수를 세면서 ice의 개수를 저장 후 update 시켜줌

def bfs(start):
    ice = defaultdict(int)
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        path.add((x, y))

        for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue

            if mat[new_x][new_y] == 0:
                ice[(x, y)] += 1
            elif (new_x, new_y) not in path:
                path.add((new_x, new_y))
                queue.append((new_x, new_y))
    return ice

N, M = map(int, input().split(' '))
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split(' '))))

# bfs를 돌면서 주변 0의 개수를 저장
days = 0
while True:
    count, path = 0, set()
    for i in range(N):
        for j in range(M):
            if mat[i][j] > 0 and (i, j) not in path:
                ice = bfs((i, j))
                count += 1

    if count >= 2:
        print(days)
        break 
    if count == 0:
        print(0)
        break

    # 0의 개수에 맞게 mat 업데이트 시켜줌
    for (x, y), cnt in ice.items():
        mat[x][y] = 0 if mat[x][y] < cnt else mat[x][y] - cnt
    days += 1

