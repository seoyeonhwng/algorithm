import heapq
from collections import defaultdict

# start ~ end까지 최단거리 + 90도 회전시 가중치 -> 다익스트라
W, H = map(int, input().split(' '))
mat = [list(input()) for _ in range(H)]

c = []
for i in range(H):
    for j in range(W):
        if mat[i][j] == 'C':
            c.append((i, j))
start, end = c[0], c[1]

heap = []
x, y = start
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= H or ny < 0 or ny >= W or mat[nx][ny] == '*':
        continue
    heapq.heappush(heap, (0, nx, ny, i))

dist = defaultdict(int)
while heap:
    cost, x, y, d = heapq.heappop(heap)
    if (x, y, d) in dist: # 방향까지 같이 저장해줘야함!!
        continue
    if (x, y) == end:
        print(cost)
        break

    dist[(x, y, d)] = cost
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W or mat[nx][ny] == '*':
            continue

        nc = cost + 1 if (d-1) % 4 == i or (d+1) % 4 == i else cost
        heapq.heappush(heap, (nc, nx, ny, i))