from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):
    queue = deque([(sx, sy)])
    dist = [[sys.maxsize] * C for _ in range(R)]
    dist[sx][sy] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if mat[nx][ny] == '1' or dist[nx][ny] != sys.maxsize:
                continue
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

    return dist


R, C = map(int, input().split(' '))
mat = [list(input()) for _ in range(R)]
x1, y1 = map(int, input().split(' '))
x2, y2 = map(int, input().split(' '))
x3, y3 = map(int, input().split(' '))

dist1 = bfs(x1-1, y1-1)
dist2 = bfs(x2-1, y2-1)
dist3 = bfs(x3-1, y3-1)

ans = defaultdict(int)
for i in range(R):
    for j in range(C):
        ans[max(dist1[i][j], dist2[i][j], dist3[i][j])] += 1

m = min(ans)
if m == sys.maxsize:
    print(-1)
else:
    print(m)
    print(ans[m])
