import heapq
from collections import defaultdict

# (sx, sy) ~ (ex, ey) 최단 거리, 거리합이 최대
# 다익스트라로 하면 첫 N-1, M-1 도달한 최단거리, 거리합 최대 알 수 있음

for t in range(int(input())):
    N, M = map(int, input().split(' '))
    sx, sy, ex, ey = map(int, input().split(' '))
    mat = [list(map(int, input().split(' '))) for _ in range(N)]

    heap = [(0, -mat[sx][sy], sx, sy)]
    dist = defaultdict(int)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    ans = -1
    while heap:
        cost, power, x, y = heapq.heappop(heap)
        if x == ex and y == ey:
            ans = -power
            break
        
        if (x, y) in dist:
            continue

        dist[(x, y)] = cost
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or mat[nx][ny] == -1:
                continue
            heapq.heappush(heap, (cost + 1, power-mat[nx][ny], nx, ny))
    print(f'Case #{t+1}: {ans}') if ans != -1 else print(f'Case #{t+1}: Mission Impossible.')

# 가중치가 없는 최단 거리 구하는 경우 bfs를 사용할 수 있다.
# 하지만 최단 거리 + 특정한 조건이 있으면 다익스트라로 풀 수 있음!!!