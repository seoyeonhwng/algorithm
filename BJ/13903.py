import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        x, y, count = queue.popleft()
        if x == R-1:
            return count
        
        for i in range(N):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mat[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True
    return -1


R, C = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(R)]
dx, dy = [], []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split(' '))
    dx.append(a)
    dy.append(b)

queue = deque()
visited = [[False] * C for _ in range(R)]

for i in range(C):
    if mat[0][i] == 1:
        queue.append((0, i, 0))
        visited[0][i] = True

print(bfs())

# bfs의 시작점이 여러개인 경우 따로 bfs할 필요없이 큐에 다 넣으면 됨!!!