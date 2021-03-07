import heapq, sys
input = sys.stdin.readline


def dijkstra():
    heap = [(mat[0][0], 0, 0)]
    dist = [[sys.maxsize] * N for _ in range(N)]
    dist[0][0] = mat[0][0]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while heap:
        cost, x, y = heapq.heappop(heap)
        if dist[x][y] != cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if dist[nx][ny] > cost + mat[nx][ny]:
                dist[nx][ny] = cost + mat[nx][ny]
                heapq.heappush(heap, (cost + mat[nx][ny], nx, ny))
    return dist

for _ in range(int(input())):
    N = int(input())
    mat = [list(map(int, input().split(' '))) for _ in range(N)]
    dist = dijkstra()
    print(dist[N-1][N-1])