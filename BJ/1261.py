import heapq
from collections import defaultdict

M, N = map(int, input().split(' '))
maps = [list(map(int, list(input()))) for _ in range(N)]

# (0, 0)부터 (N-1, M-1)까지 최소 벽 부수는 개수 = 벽을 부숴야할때 +1 -> 다익스트라
heap = [(0, 0, 0)]
dist = defaultdict(int)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    cost, x, y = heapq.heappop(heap)
    if (x, y) in dist:
        continue

    dist[(x, y)] = cost
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        new_cost = cost if maps[nx][ny] == 0 else cost + 1
        heapq.heappush(heap, (new_cost, nx, ny))
print(dist[(N-1, M-1)])