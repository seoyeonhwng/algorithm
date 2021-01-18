from collections import deque

def bfs():
    queue = deque([(sx-1, sy-1, sd, 0)])
    visited = set([(sx-1, sy-1, sd)])

    while queue:
        x, y, d, count = queue.popleft()
        if (x, y, d) == (ex-1, ey-1, ed):
            return count

        # 현재 방향으로 1, 2, 3만큼 이동
        for k in [1, 2, 3]:
            nx, ny = x + k * dx[d], y + k * dy[d]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or (nx, ny, d) in visited:
                continue
            if mat[nx][ny] == 1:
                break
            queue.append((nx, ny, d, count + 1))
            visited.add((nx, ny, d))
        
        # 오른쪽 회전, 왼쪽 회전
        for nd in [(d + 3) % 4, (d + 1) % 4]:
            if (x, y , nd) in visited:
                continue
            queue.append((x, y, nd, count + 1))
            visited.add((x, y, nd))


def convert_d(d):
    if d == 1: # 동
        return 0
    if d == 2: # 서
        return 2
    if d == 3: # 남
        return 3
    if d == 4: # 북
        return 1


M, N = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(M)]
sx, sy, sd = map(int, input().split(' '))
ex, ey, ed = map(int, input().split(' '))

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# (sx, sy, sd)에서 (ex, ey, ed)로 최단 거리 -> BFS!!!
sd, ed = convert_d(sd), convert_d(ed)
print(bfs())
