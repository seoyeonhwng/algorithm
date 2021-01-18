from collections import deque
import sys


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dx_h = [2, 2, -2, -2, 1, -1, 1, -1]
dy_h = [1, -1, 1, -1, 2, 2, -2, -2]

def bfs():
    queue = deque([(0, 0, K, 0)])
    visited = set([(0, 0, K)]) # K가 얼마일때 방문했는지도 같이 저장!

    while queue:
        x, y, k, count = queue.popleft()
        if x == H-1 and y == W-1:
            return count

        # 상하좌우
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if mat[nx][ny] == 1 or (nx, ny, k) in visited:
                continue
            queue.append((nx, ny, k, count + 1))
            visited.add((nx, ny, k))
        
        # 말 이동
        if k == 0:
            continue
        for i in range(8):
            nx, ny = x + dx_h[i], y + dy_h[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if mat[nx][ny] == 1 or (nx, ny, k-1) in visited:
                continue
            queue.append((nx, ny, k-1, count + 1))
            visited.add((nx, ny, k-1))

    return -1


K = int(input())
W, H = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(H)]

# (0, 0)부터 (H-1, W-1)까지 최단 거리 -> BFS!!
print(bfs())