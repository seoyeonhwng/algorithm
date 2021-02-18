from collections import deque

def bfs():
    queue = deque([(sx-1, sy-1, 1, 0)])
    visited = set([(sx-1, sy-1, 1)])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, k, count = queue.popleft()
        if (x, y) == (ex-1, ey-1):
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == 0 and (nx, ny, k) not in visited:
                queue.append((nx, ny, k, count + 1))
                visited.add((nx, ny, k))

            if mat[nx][ny] == 1 and k == 1 and (nx, ny, k-1) not in visited:
                queue.append((nx, ny, k-1, count + 1))
                visited.add((nx, ny, k-1))
    return -1


N, M = map(int, input().split(' '))
sx, sy = map(int, input().split(' '))
ex, ey = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# (sx, sy)부터 (ex, ey)까지 최단 거리 -> bfs!!
# 0은 빈칸, 1은 벽 + 벽은 한번 부술수 있음!
print(bfs())