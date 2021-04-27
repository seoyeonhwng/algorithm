from collections import deque
import sys

def bfs(num):
    # label에서 num인 땅에서 bfs로 다른 땅을 만나는지
    queue = deque()
    for i in range(N):
        for j in range(M):
            if label[i][j] == num:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny, d = x, y, 0
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                if label[nx][ny] == num:
                    break

                # 다른 섬에 도달한 경우
                if label[nx][ny] > 0 and label[nx][ny] != num:
                    if d >= 2: # 길이가 2이상인 경우만 다리를 놓을 수 있으므로 갱신
                        dist[label[nx][ny]-1][num-1] = min(dist[label[nx][ny]-1][num-1], d)
                        dist[num-1][label[nx][ny]-1] = min(dist[num-1][label[nx][ny]-1], d)
                    break
                d += 1

def dfs(i, j, l):
    if i < 0 or i >= N or j < 0 or j >= M or mat[i][j] == 0:
        return
    
    mat[i][j] = 0
    label[i][j] = l
    dfs(i+1, j, l)
    dfs(i-1, j, l)
    dfs(i, j+1, l)
    dfs(i, j-1, l)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# 섬 라벨링
label, l, count = [[0] * M for _ in range(N)], 1, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            dfs(i, j, l)
            l += 1
            count += 1

# 각 섬 사이의 최단 거리를 구함
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dist = [[sys.maxsize] * count for _ in range(count)]
for n in range(1, count+1):
    bfs(n)

edges = []
for i in range(count):
    for j in range(i+1, count):
        if dist[i][j] != sys.maxsize:
            edges.append((dist[i][j], i, j))

edges.sort()
parent = [i for i in range(count)]
answer = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

# 모두 연결되어있다면 모든 섬의 부모가 같음!
check = set([find_parent(i) for i in range(count)])
if len(check) == 1:
    print(answer)
else:
    print(-1)