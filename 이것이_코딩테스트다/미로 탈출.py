from collections import deque

def bfs():
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (N-1, M-1):
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == 0 or (nx, ny) in visited:
                continue

            queue.append((nx, ny, count + 1))
            visited.add((nx, ny))


N, M = map(int, input().split(' '))
mat = [list(map(int, input())) for _ in range(N)]

# (1, 1)에서부터 (N, M)까지 최단 거리 -> BFS!!
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs())