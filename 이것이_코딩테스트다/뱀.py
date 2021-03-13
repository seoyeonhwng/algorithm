from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 0, 0, [(0, 0)])])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y, d, time, body = queue.popleft()

        # 방향 바꾸기
        if rotation and rotation[0][0] == time:
            _, c = rotation.popleft()
            d = (d + 3) % 4 if c == 'L' else (d + 1) % 4

        nx, ny = x + dx[d], y + dy[d]
        # 벽 또는 자기 자신의 몸과 부딪히면 게임 끝
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ((nx, ny) in body):
            return time + 1

        body = body if mat[nx][ny] == 1 else body[:-1]
        mat[nx][ny] = 0
        queue.append((nx, ny, d, time + 1, [(nx, ny)] + body))



N = int(input())

mat = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    x, y = map(int, input().rstrip().split(' '))
    mat[x-1][y-1] = 1

rotation = deque()
for _ in range(int(input())):
    t, d = input().rstrip().split(' ')
    rotation.append((int(t), d))

print(bfs())