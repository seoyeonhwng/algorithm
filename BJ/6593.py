from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(s):
    queue = deque([(s[0], s[1], s[2], 0)])
    visited = set([s])

    while queue:
        x, y, z, count = queue.popleft()
        if (x, y, z) == end:
            return f'Escaped in {count} minute(s).'
        
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C:
                continue
            if mat[nx][ny][nz] == '#' or (nx, ny, nz) in visited:
                continue
            queue.append((nx, ny, nz, count + 1))
            visited.add((nx, ny, nz))
    return 'Trapped!'

while True:
    L, R, C = map(int, input().split(' '))
    if L == 0 and R == 0 and C == 0:
        break

    mat = []
    for _ in range(L):
        mat.append([list(input()) for _ in range(R)])
        input()

    # S에서 E까지 최단 거리 구한다! -> BFS!!
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if mat[i][j][k] == 'S':
                    start = (i, j, k)
                elif mat[i][j][k] == 'E':
                    end = (i, j, k)

    print(bfs(start))