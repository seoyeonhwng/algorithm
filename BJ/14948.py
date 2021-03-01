import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, level[0][0], 1)])
    visited = [[[sys.maxsize] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = level[0][0] # (i, j)끼지 오는데 필요한 최소 레벨 -> 스킵 가능한 경우는 무조건 이런식으로!

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, l, k = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny][k] > max(l, level[nx][ny]):
                queue.append((nx, ny, max(l, level[nx][ny]), k))
                visited[nx][ny][k] = max(l, level[nx][ny])

            # 해당 방향으로 한칸 이동 (타일을 도중에 뛰어넘을 수 없다는 조건 때문에 이렇게 하는 듯..?)
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if k == 1 and visited[nx][ny][k-1] > max(l, level[nx][ny]):
                queue.append((nx, ny, max(l, level[nx][ny]), k-1))
                visited[nx][ny][k-1] = max(l, level[nx][ny])

    return min(visited[N-1][M-1])



N, M = map(int, input().rstrip().split(' '))
level = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

print(bfs())