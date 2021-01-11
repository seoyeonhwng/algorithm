from collections import deque

def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = set([(i, j)])
    depth = 0

    while queue:
        x, y, count = queue.popleft()
        depth = max(depth, count)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if (nx, ny) in visited or mat[nx][ny] == 'W':
                continue

            queue.append((nx, ny, count + 1))
            visited.add((nx, ny))
    return depth



N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 'L'이면 bfs해서 가장 max값을 구한다
ans = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)