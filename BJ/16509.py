from collections import deque

def get_candi(x, y, i):
    info = {
        0 : [(-1, 0), (-1, 1), (-1, 1)],
        1 : [(-1, 0), (-1, -1), (-1, -1)],
        2 : [(0, 1), (-1, 1), (-1, 1)],
        3 : [(0, 1), (1, 1), (1, 1)],
        4 : [(0, -1), (-1, -1), (-1, -1)],
        5 : [(0, -1), (1, -1), (1, -1)],
        6 : [(1, 0), (1, -1), (1, -1)],
        7 : [(1, 0), (1, 1), (1, 1)]
    }
    candi, nx, ny = [], x, y
    for dx, dy in info[i]:
        nx, ny = nx + dx, ny + dy
        candi.append((nx, ny))
    return candi

def can_go(x, y, i): # (x, y)에서 i번쨰 방향으로 갈수 있는지 체크
    candi = get_candi(x, y, i)
    for i, (cx, cy) in enumerate(candi):
        if cx < 0 or cx >= 10 or cy < 0 or cy >= 9:
            return False
        if i < 2 and (cx, cy) == (R2, C2):
            return False
    return True

def bfs():
    queue = deque([(R1, C1, 0)])
    visited = [[False] * 9 for _ in range(10)]
    visited[R1][C1] = True

    dx = [-3, -3, -2, 2, -2, 2, 3, 3]
    dy = [2, -2, 3, 3, -3, -3, -2, 2]

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (R2, C2):
            return count

        for i in range(8):
            if not can_go(x, y, i):
                continue

            nx, ny = x + dx[i], y + dy[i]
            if not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

    return -1


R1, C1 = map(int, input().split(' '))
R2, C2 = map(int, input().split(' '))
print(bfs())