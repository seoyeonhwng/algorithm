from collections import deque

def bfs():
    queue = deque([(r1-1, c1-1)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        if (x, y) == (r2-1, c2-1):
            if mat[x][y] == 'X':
                return 'YES'
            mat[x][y] = 'X'
            queue.append((x, y))
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == 'X':
                continue

            queue.append((nx, ny))
            mat[x][y] = 'X'
    return 'NO'

N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

r1, c1 = map(int, input().rstrip().split(' '))
r2, c2 = map(int, input().rstrip().split(' '))

# (r1, c1)에서 (r2, c2)까지의 이동 가능 여부 -> bfs!!
# X로 이동할 수 없고 이동하고 나면 원래 좌표는 X가 됨!
print(bfs())