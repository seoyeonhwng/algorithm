import heapq
from collections import defaultdict

count = 0
while True:
    count += 1
    N = int(input())
    if N == 0:
        break
    maps = [list(map(int, input().split(' '))) for _ in range(N)]

    # (0, 0) ~ (N-1, N-1)까지의 최단 거리 + 가중치 -> 다익스트라
    heap = [(maps[0][0], 0, 0)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
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
            heapq.heappush(heap, (cost + maps[nx][ny], nx, ny))

    print(f'Problem {count}: {dist[(N-1, N-1)]}')