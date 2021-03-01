from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, K, 1, True)])
    dp = [[[sys.maxsize] * (K+1) for _ in range(M)] for _ in range(N)]
    dp[0][0][K] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, k, count, is_day = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if mat[nx][ny] == '0' and dp[nx][ny][k] > count + 1: # 벽 안부수는 경우
                dp[nx][ny][k] = count + 1
                queue.append((nx, ny, k, count + 1, not is_day))

            if mat[nx][ny] == '1' and k > 0 and dp[nx][ny][k-1] > count + 1: # 벽 부수는 경우
                if is_day: # 낮이면 부숨
                    dp[nx][ny][k-1] = count + 1
                    queue.append((nx, ny, k-1, count + 1, not is_day))
                else: # 하루 기다림
                    dp[x][y][k] = count + 1
                    queue.append((x, y, k, count + 1, not is_day))
    return dp
    

N, M, K = map(int, input().split(' '))
mat = [list(input()) for _ in range(N)]

dp = bfs()
ans = min(dp[N-1][M-1])
print(-1) if ans == sys.maxsize else print(ans)