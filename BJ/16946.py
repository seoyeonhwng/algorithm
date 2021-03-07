import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(sx, sy, label):
    queue = deque([(sx, sy)])
    visited[sx][sy] = label
    count = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] != 0 or visited[nx][ny] != -1:
                continue

            visited[nx][ny] = label
            queue.append((nx, ny))
            count = (count + 1) % 10
    return (count + 1) % 10

def get_count(x, y):
    idx, count = set(), 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] != -1:
            idx.add(visited[nx][ny])

    for i in idx:
        count += index[i]
    return count
      


N, M = map(int, input().split(' '))
mat = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 0마다 bfs해서 넘버링
visited = [[-1] * M for _ in range(N)]
index = defaultdict(int)
label = 1
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0 and visited[i][j] == -1:
            cnt = bfs(i, j, label)
            index[label] = cnt
            label += 1

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            mat[i][j] = (get_count(i, j) + 1) % 10

for row in mat:
    print(''.join([str(r) for r in row]))

