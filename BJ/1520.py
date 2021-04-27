def dfs(x, y):
    # dp[x][y] = (x, y)에서 (0, 0)까지 가는 경우의 수
    if (x, y) == (0, 0): # 기저 조건
        return 1
    if dp[x][y] != -1: # 이미 dp값이 게산된 경우 -> 바로 리턴해서 중복해서 계산하지 않음
        return dp[x][y]

    # 처음으로 dp[x][y]를 계산함 -> 0으로 초기화
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or mat[nx][ny] <= mat[x][y]:
            continue
        dp[x][y] += dfs(nx, ny)
    return dp[x][y]
    

N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[-1] * M for _ in range(N)] # 경우의 수가 0개인지 첫방문인지 구별하기 위해 -1로 초기화!!
print(dfs(N-1, M-1))