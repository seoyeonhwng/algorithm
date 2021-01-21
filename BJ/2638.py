from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny) in visited:
                continue

            if mat[nx][ny] == 0:
                queue.append((nx, ny))
                visited.add((nx, ny))
            else:
                mat[nx][ny] += 1

def melt():
    count = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] >= 3: # 녹음
                mat[i][j] = 0
                count += 1
            elif mat[i][j] > 1:
                mat[i][j] = 1
    return count

N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# (0, 0)을 시작으로 BFS -> 인접한 칸이 0이면 큐에 넣고 치즈이면 해당 값을 +1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

while True:
    bfs()
    if melt() == 0:
        print(ans)
        break
    ans += 1