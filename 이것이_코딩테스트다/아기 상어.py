from collections import deque
import heapq


def bfs(sx, sy):
    # (sx, sy)에서 갈 수 있는 물고기 리스트를 구해서 반환
    heap = []
    queue = deque([(sx, sy, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    mat[sx][sy] = 0

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or mat[nx][ny] > size:
                continue

            if mat[nx][ny] == 0 or mat[nx][ny] == size: # 이동
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True
            else: # 먹을 수 있는 물고기 -> 먹고 이동하지 않고 여기서 스탑
                heapq.heappush(heap, (count + 1, nx, ny))
    return heap


N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            x, y = i, j

ans, size, eat = 0, 2, 0
while True:
    # 가능한 물고기 위치를 찾음
    fish_list = bfs(x, y)
    if not fish_list:
        break
    
    # 해당 물고기를 먹음
    dist, nx, ny = fish_list[0]
    ans += dist
    eat += 1

    if size == eat:
        size, eat = size + 1, 0

    x, y = nx, ny

print(ans)
