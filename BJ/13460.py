from collections import deque

def bfs(bx, by, rx, ry):
    queue = deque([(bx, by, 0, 'B'), (rx, ry, 0, 'R')])
    rvisited[rx][ry] = True
    bvisited[bx][by] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, count, t = queue.popleft()
        print('+++', x, y, count, t)
        if (count > 10) or ((x, y) == (hx, hy) and t == 'B'):
            return -1
        if (x, y) == (hx, hy) and t == 'R':
            return count

        for i in range(4):
            op_ball = (bx, by) if t == 'R' else (rx, ry)
            visited = rvisited if t == 'R' else bvisited
            
            nx, ny = x + dx[i], y + dy[i]   
            while 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == '.' and (nx, ny) != op_ball:
                nx, ny = nx + dx[i], ny + dy[i]

            if not visited[nx][ny] and mat[nx][ny] == '.':
                queue.append((nx, ny, count + 1, t))
                visited[nx][ny] = True
            
            if t == 'R':
                rx, ry = nx, ny
            else:
                bx, by = nx, ny
    return -1


N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if mat[i][j] == 'R':
            rx, ry = i, j
        elif mat[i][j] == 'B':
            bx, by = i, j
        elif mat[i][j] == 'O':
            hx, hy = i, j

rvisited = [[False] * M for _ in range(N)]
bvisited = [[False] * M for _ in range(N)]
print(bfs(bx, by, rx, ry))