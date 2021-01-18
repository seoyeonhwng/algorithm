from collections import deque

def bfs():
    queue = deque([(0, 0, 1, 1)])
    visited = set([(0, 0, 1)])

    while queue:
        x, y, k, count = queue.popleft()
        if (x, y) == (N-1, M-1):
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny, k) in visited:
                continue
            if mat[nx][ny] == 1 and k == 1 and (nx, ny, k-1) not in visited:
                queue.append((nx, ny, k-1, count+1))
                visited.add((nx, ny, k-1))
            if mat[nx][ny] == 0:
                queue.append((nx, ny, k, count+1))
                visited.add((nx, ny, k))
    return -1


N, M = map(int, input().split(' ')) 
mat = [list(map(int, input())) for _ in range(N)]

# (1, 1)부터 (N, M)까지 최단 거리 -> BFS!!!
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs())