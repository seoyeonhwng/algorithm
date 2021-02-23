import heapq
from collections import defaultdict

def dijkstra():
    heap = [(level[0][0], 0, 0)]
    dist = defaultdict(int)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while heap:
        l, x, y = heapq.heappop(heap)
        if (x, y) == (N-1, M-1):
            return l

        if (x, y) in dist:
            continue

        dist[(x, y)] = l
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            heapq.heappush(heap, (max(l, level[nx][ny]), nx, ny))


N, M = map(int, input().split(' '))
level = [list(map(int, input().split(' '))) for _ in range(N)]

print(dijkstra())