from collections import deque
import sys
input = sys.stdin.readline

def convert_pos(x, y):
    nx, ny = y-1, x-1
    return W-1-nx, ny

def bfs():
    queue = deque([(sx, sy, mat[sx][sy])])
    visited = set([(sx, sy)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, c = queue.popleft()
        if (x, y) == (ex, ey):
            return 'YES'

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= W or ny < 0 or ny >= L:
                continue
            if (nx, ny) in visited or mat[nx][ny] != c:
                continue
            queue.append((nx, ny, mat[nx][ny]))
            visited.add((nx, ny))
    return 'NO'

for _ in range(int(input())):
    L, W, A, B, C, D = map(int, input().split(' '))
    mat = [list(input()) for _ in range(W)]

    sx, sy = convert_pos(A, B)
    ex, ey = convert_pos(C, D)

    print(bfs())