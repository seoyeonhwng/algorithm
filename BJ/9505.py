from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, sx, sy)]
    dist = [[sys.maxsize] * W for _ in range(H)] # (sx, sy)부터 해당 칸까지 최단 거리를 저장
    dist[sx][sy] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while heap:
        count, x, y = heapq.heappop(heap)
        if x == 0 or x == H-1 or y == 0 or y == W-1:
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if dist[nx][ny] > count + info[mat[nx][ny]]:
                dist[nx][ny] = count + info[mat[nx][ny]]
                heapq.heappush(heap, (dist[nx][ny], nx, ny))   


for _ in range(int(input())):
    K, W, H = map(int, input().split(' '))
    info = defaultdict(int)
    for _ in range(K):
        name, time = input().split(' ')
        info[name] = int(time)

    mat = [list(input()) for _ in range(H)]

    # E부터 가장자리까지의 최단 거리 -> 다익스트라!
    for i in range(H):
        for j in range(W):
            if mat[i][j] == 'E':
                sx, sy = i, j
                break
    print(dijkstra())

    # 다익스트라 풀때 이차원 배열이라면 배열에 최단 거리를 저장해가면서 푼다 + 힙에 넣을때 최소 거리보다 작은 경우만 넣는다!