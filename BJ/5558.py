from collections import deque

def bfs(start, end):
    # start - end까지의 최단 거리를 구함!
    sx, sy = pos[start]
    queue = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == pos[end]:
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if (nx, ny) in visited or mat[nx][ny] == 'X':
                continue
            queue.append((nx, ny, count + 1))
            visited.add((nx, ny))
            

H, W, N = map(int, input().split(' '))
mat = [list(input()) for _ in range(H)]

pos = {}
for i in range(H):
    for j in range(W):
        if mat[i][j] == '.' or mat[i][j] == 'X':
            continue
        pos[mat[i][j]] = (i, j)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

node = ['S'] + [str(i + 1) for i in range(N)]
ans = 0
for i in range(N):
    ans += bfs(node[i], node[i+1])
print(ans)