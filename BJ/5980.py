from collections import defaultdict, deque
import sys

def get_opposite(c, x, y):
    for slide in slides[c]:
        if slide != (x, y):
            return slide

def bfs():
    queue = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == (ex, ey):
            return count

        # 상하좌우 갈 수 있음 단 가고자하는 곳이 슬라이드라면 반대편 위치를 삽입 (슬라이드는 재사용가능하므로 방문처리 안함)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if mat[nx][ny] == '#' or (nx, ny) in visited:
                continue

            if 'A' <= mat[nx][ny] <= 'Z':
                nx, ny = get_opposite(mat[nx][ny], nx, ny)
            else:
                visited.add((nx, ny))
            queue.append((nx, ny, count + 1))

 

N, M = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

# @부터 =까지 최단 거리 + #는 갈 수 없음
# 현재 위치가 .면 상하좌우로 이동 + 현재 위치가 대문자영어라면 반대쪽 쌍으로 이동 가능
# 목적지까지 최단 거리 -> bfs!!

slides = defaultdict(list)
for i in range(N):
    for j in range(M):
        if mat[i][j] == '@':
            sx, sy = i, j
        elif mat[i][j] == '=':
            ex, ey = i, j
        elif 'A' <= mat[i][j] <='Z':
            slides[mat[i][j]].append((i, j))

print(bfs())