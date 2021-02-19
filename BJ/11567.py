from collections import deque

def bfs():
    queue = deque([(r1-1, c1-1)])
    mat[r1-1][c1-1] = 'X'
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if (nx, ny) == (r2-1, c2-1):
                if mat[nx][ny] == 'X':
                    return 'YES'
            
            if mat[nx][ny] == '.':
                queue.append((nx, ny))
                mat[nx][ny] = 'X'
    return 'NO'



N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]
r1, c1 = map(int, input().rstrip().split(' '))
r2, c2 = map(int, input().rstrip().split(' '))

# (r1, c1)에서 (r2, c2)까지 도달 가능한지 -> bfs
print(bfs())
