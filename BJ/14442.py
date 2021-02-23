from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, K, 0)])
    visited = [[[sys.maxsize] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, k, count = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if mat[nx][ny] == '0' and visited[nx][ny][k] > count + 1:
                queue.append((nx, ny, k, count + 1))
                visited[nx][ny][k] = count + 1
            if mat[nx][ny] == '1' and k > 0 and visited[nx][ny][k-1] > count + 1:
                queue.append((nx, ny, k - 1, count + 1))
                visited[nx][ny][k-1] = count + 1
    return visited[N-1][M-1]

N, M, K = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

dp = bfs()
ans = min(dp)
print(-1) if ans == sys.maxsize else print(ans + 1)