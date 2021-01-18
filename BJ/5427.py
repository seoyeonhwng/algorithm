from collections import deque

def fill_fire(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if mat[nx][ny] == '#' or fire[nx][ny] != -1:
                continue
            queue.append((nx, ny))
            fire[nx][ny] = fire[x][y] + 1

# 상근이의 이동
def bfs(sx, sy):
    queue = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])

    while queue:
        x, y, count = queue.popleft()
        if x == 0 or x == H-1 or y == 0 or y == W-1:
            return count + 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or (nx, ny) in visited:
                continue
            
            # 불 또는 불이 붙은 칸 , 벽을 갈 수 없음1
            if fire[nx][ny] != -1 and fire[nx][ny] <= count+1: # count+1로 비교하는거 잊지말자!!!
                continue
            if mat[nx][ny] == '#':
                continue 
            queue.append((nx, ny, count + 1))
            visited.add((nx, ny))

    return "IMPOSSIBLE"

for _ in range(int(input())):
    W, H = map(int, input().split(' '))
    mat = [list(input()) for _ in range(H)]

    fire = [[-1] * W for _ in range(H)]
    fire_queue = deque()

    for i in range(H):
        for j in range(W):
            if mat[i][j] == '@':
                sx, sy = i, j
            elif mat[i][j] == '*':
                fire_queue.append((i, j))
                fire[i][j] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    fill_fire(fire_queue)
    print(bfs(sx, sy))


