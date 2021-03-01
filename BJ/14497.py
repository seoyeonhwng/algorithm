from collections import deque

def bfs():
    queue = deque([(x1-1, y1-1, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[x1-1][y1-1] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (x2-1, y2-1):
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue

            if mat[nx][ny] == '0':
                queue.appendleft((nx, ny, count))
            else:
                queue.append((nx, ny, count + 1))
            visited[nx][ny] = True


N, M = map(int, input().split(' '))
x1, y1, x2, y2 = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

print(bfs())