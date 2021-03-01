from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, mat[0][0])])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    dx = [0, 1]
    dy = [1, 0]

    while queue:
        x, y, k = queue.popleft()
        if (x, y) == (N-1, N-1):
            return 'HaruHaru'
        
        for i in range(2):
            nx, ny = x + (k * dx[i]), y + (k * dy[i])
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            
            queue.append((nx, ny, mat[nx][ny]))
            visited[nx][ny] = True
    return 'Hing'


N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]
print(bfs())