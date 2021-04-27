import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    if dp[x][y]: # 이미 계산한 적이 있다면
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or mat[x][y] >= mat[nx][ny]:
            continue
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

# 매 지점에서 dfs를 했을때 갈 수 있는 최장거리
# 경우의 수가 엄청 많음!!! -> dp를 생각하자
# dp[x][y]에는 (x, y)에서 출발했을때 최장거리를 저장
# dp[x][y]는 max(가능한 상하좌우) + 1

N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[0] * N for _ in range(N)]
answer = 1
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
print(answer)
