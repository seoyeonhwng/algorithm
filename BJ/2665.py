import heapq
from collections import defaultdict

# 검정색을 지날때 값 +1 -> 다익스트라!!
N = int(input())
maps = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
heap = [(0, 0, 0)]
dist = defaultdict(int)
while heap:
    cost, x, y = heapq.heappop(heap)
    if (x, y) in dist:
        continue

    dist[(x, y)] = cost
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        new_cost = cost if maps[nx][ny] == 1 else cost + 1
        heapq.heappush(heap, (new_cost, nx, ny))
print(dist[(N-1, N-1)])