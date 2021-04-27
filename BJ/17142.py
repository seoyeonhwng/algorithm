from itertools import combinations
from collections import deque
import sys

def bfs(viruses):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    for x, y in viruses:
        queue.append((x, y, 0))
        dist[x][y] = 0

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or mat[nx][ny] == 1:
                continue

            # 빈 칸인 경우
            if dist[nx][ny] > count + 1:
                dist[nx][ny] = count + 1
                queue.append((nx, ny, count + 1))


def get_max_day(dist):
    # 최대 시간을 확인 + 바이러스가 다 퍼졌는지
    answer = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                if dist[i][j] == sys.maxsize:
                    return -1
                answer = max(answer, dist[i][j])
    return answer
            


N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 2:
            virus.append((i, j))

answer = sys.maxsize
for candi in list(combinations(virus, M)):
    dist = [[sys.maxsize] * N for _ in range(N)]
    bfs(candi)

    max_day = get_max_day(dist)
    if max_day != -1:
        answer = min(answer, max_day)
print(-1) if answer == sys.maxsize else print(answer)