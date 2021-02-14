from collections import deque

def bfs():
    queue = deque([(sx, sy, 0)])
    visited = set()

    while queue:
        x, y, dist = queue.popleft()
        if mat[x][y] == 'G':
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mat[nx][ny] == 'X' or (nx, ny) in visited:
                continue
            queue.append((nx, ny, dist + 1))
            visited.add((nx, ny))
    return -1

for _ in range(int(input())):
    R, C = map(int, input().split(' '))
    mat = [list(input()) for _ in range(R)]

    # S에서 G까지 최댠 거리 -> bfs!!
    for i in range(R):
        for j in range(C):
            if mat[i][j] == 'S':
                sx, sy = i, j
                break

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = bfs()
    print(f'Shortest Path: {ans}') if ans != -1 else print('No Exit')

