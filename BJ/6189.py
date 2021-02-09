from collections import deque

R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]
 # C에서 B까지 최단거리 -> bfs

for i in range(R):
    for j in range(C):
        if mat[i][j] == 'B':
            end = (i, j)
        elif mat[i][j] == 'C':
            start = (i, j)

queue = deque([(start[0], start[1], 0)])
visited = set([(start[0], start[1])])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y, dist = queue.popleft()
    if (x, y) == end:
        print(dist)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if (nx, ny) in visited or mat[nx][ny] != '*':
            continue
        queue.append((nx, ny, dist + 1))
        visited.add((nx, ny))