import heapq
from collections import defaultdict

def dijkstra():
    heap = [(0, -mat[sx][sy], sx, sy)]
    dist = defaultdict(int)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while heap:
        count, power, x, y = heapq.heappop(heap)
        if (x, y) == (ex, ey):
            return -power

        if (x, y) in dist:
            continue

        dist[(x, y)] = count
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == -1:
                continue
            heapq.heappush(heap, (count+1, power-mat[nx][ny], nx, ny))
    return -1

# (sx, sy) ~ (ex, ey)까지 최단 횟수 거리로 이동 + power를 최대한!! -> 다익스트라
for i in range(int(input())):
    N, M = map(int, input().split(' '))
    sx, sy, ex, ey = map(int, input().split(' '))
    mat = [list(map(int, input().split(' '))) for _ in range(N)]

    ans = dijkstra()
    print(f'Case #{i+1}: Mission Impossible.') if ans == -1 else print(f'Case #{i+1}: {ans}')