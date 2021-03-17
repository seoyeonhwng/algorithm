from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    for tx, ty in teacher:
        visited[tx][ty] = True
        for d in range(4):
            queue.append((tx, ty, d))

    while queue:
        x, y, d = queue.popleft()

        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx, ny) in obs:
            continue
        
        visited[nx][ny] = True
        queue.append((nx, ny, d))


N = int(input())
mat = [list(input().rstrip().split(' ')) for _ in range(N)]

student, teacher, empty = [], [], []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'S':
            student.append((i, j))
        elif mat[i][j] == 'T':
            teacher.append((i, j))
        else:
            empty.append((i, j))

for obs in combinations(empty, 3):
    visited = [[False] * N for _ in range(N)]
    bfs()

    possible = True
    for sx, sy in student: # 한명이라도 도달가능하면 안됨
        if visited[sx][sy]:
            possible = False
            break

    if possible:
        print('YES')
        break
else:
    print('NO')