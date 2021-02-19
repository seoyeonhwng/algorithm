from collections import deque

def bfs(sx, sy): 
    # (i, j)에서 출발해서 바깥까지! 벽 이동못하고 문은 열어주기
    queue = deque([(sx, sy, 0, [])])
    visited = set([(sx, sy)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, count, door = queue.popleft()
        if x == 0 or x == H-1 or y == 0 or y == W-1:
            return door
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if mat[nx][ny] == '*' or (nx, ny) in visited:
                continue

            if mat[nx][ny] == '.' or mat[nx][ny] == '$':
                queue.appendleft((nx, ny, count, door))
            else:
                queue.append((nx, ny, count + 1, door + [(nx, ny)]))
            visited.add((nx, ny))


H, W = map(int, input().split(' '))
mat = [list(input()) for _ in range(H)]

ans = []
for i in range(H):
    for j in range(W):
        if mat[i][j] == '$':
            ans += bfs(i, j)
print(set(ans))