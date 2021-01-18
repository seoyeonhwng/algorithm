from collections import deque
import sys

def fill_water(queue):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mat[nx][ny] in ['X', 'D'] or water[nx][ny] != -1:
                continue
            
            queue.append((nx, ny))
            water[nx][ny] = water[x][y] + 1

def bfs():
    queue = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (ex, ey):
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mat[nx][ny] == 'X' or (nx, ny) in visited:
                continue

            if water[nx][ny] == -1 or water[nx][ny] > count + 1: # 물이 닿을 수 없는 곳이거나 나중에 물이 차오는 곳인 경우
                queue.append((nx, ny, count + 1))
                visited.add((nx, ny))
    return "KAKTUS"



R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]


water, queue = [[-1] * C for _ in range(R)], deque()
for i in range(R):
    for j in range(C):
        if mat[i][j] == 'S':
            sx, sy = i, j
        elif mat[i][j] == 'D':
            ex, ey = i, j
        elif mat[i][j] == '*':
            water[i][j] = 0
            queue.append((i, j))
            

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

fill_water(queue)
print(bfs())