N, M = map(int, input().split(' '))
mat = [list(map(int, input().split(' '))) for _ in range(N)]

# dp : 각 위치에서의 최대 사탕 개수
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = mat[i-1][j-1] + max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[N][M])