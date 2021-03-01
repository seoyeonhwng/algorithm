from collections import deque, defaultdict
import sys, heapq
input = sys.stdin.readline

def get_deletas(d):
    deletas = set()
    for i in range(d+1):
        deletas.add((i, d-i))
        deletas.add((i, -d+i))
        deletas.add((-i, d-i))
        deletas.add((-i, -d+i))
    return deletas

def fire(queue):
    while queue:
        x, y, t, d = queue.popleft()
        for dx, dy in get_deletas(d):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if f_map[nx][ny] > t + d:
                f_map[nx][ny] = t + d
                queue.append((x, y, t, d + 1))

def bfs():
    queue = deque([(X-1, Y-1, 0)])
    visited = [[sys.maxsize] * N for _ in range(M)]
    visited[X-1][Y-1] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if (visited[nx][ny] > count + 1) and (f_map[nx][ny] > count + 1) and ((nx, ny) not in f_xy):
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = count + 1
                
    return visited


M, N, V = map(int, input().rstrip().split(' '))
X, Y = map(int, input().rstrip().split(' '))
heights = [list(map(int, input().rstrip().split(' '))) for _ in range(M)]

queue = deque()
f_map = [[sys.maxsize] * N for _ in range(M)]
f_xy = set()
for _ in range(V):
    x, y, t = map(int, input().split(' '))
    f_xy.add((x-1, y-1))
    queue.append((x-1, y-1, t, 0))

fire(queue)
visited = bfs()

# 도달할 수 있는 가장 높은 곳의 위치, 최단 거리
ans = defaultdict(list)
for i in range(N):
    for j in range(M):
        if visited[i][j] == sys.maxsize:
            continue
        ans[heights[i][j]].append((visited[i][j]))

max_h = max(ans)
min_d = min(ans[max_h])
print(max_h, min_d)
