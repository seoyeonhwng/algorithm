from collections import deque
import sys

def get_idx(t):
    if t == 'B':
        dx = [0, 0, 1, -1, 1, 1, -1, -1]
        dy = [1, -1, 0, 0, -1, 1, 1, -1]
    else:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
    return dx, dy


def bfs(sx, sy, t):
    queue = deque([(sx, sy, 0)])
    visited = [[False] * 1000 for _ in range(1000)]
    visited[sx][sy] = True

    dx, dy = get_idx(t)
    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (jx-1, jy-1):
            return count

        N = len(dx)
        for i in range(N):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 1000 or ny < 0 or ny >= 1000 or visited[nx][ny]:
                continue

            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True



bx, by = map(int, input().split(' '))
dx, dy = map(int, input().split(' '))
jx, jy = map(int, input().split(' '))

b = bfs(bx-1, by-1, 'B')
d = bfs(dx-1, dy-1, 'D')
if b < d:
    print('bessie')
elif b == d:
    print('tie')
else:
    print('daisy')