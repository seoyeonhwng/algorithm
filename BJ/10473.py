import heapq
from collections import defaultdict

def dijkstra():
    heap = [(0, sx, sy)]
    dist = defaultdict(int)
    dx = [0, 0, 0.1, -0.1]
    dy = [0.1, -0.1, 0, 0]
    c_dx = [0, 0, 50, -50]
    c_dy = [50, -50, 0, 0]

    while heap:
        time, x, y = heapq.heappop(heap)
        if (x, y) in dist:
            continue
        if (x, y) == (ex, ey):
            return time

        dist[(x, y)] = time
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            heapq.heappush(heap, (time + 0.02, nx, ny))
        
        if (x, y) in cannon:
            for i in range(4):
                nx, ny = x + c_dx[i], y + c_dy[i]
                heapq.heappush(heap, (time + 2, nx, ny))


sx, sy = map(float, input().split(' '))
ex, ey = map(float, input().split(' '))
N = int(input())
cannon = [list(map(float, input().split(' '))) for _ in range(N)]

print(dijkstra())