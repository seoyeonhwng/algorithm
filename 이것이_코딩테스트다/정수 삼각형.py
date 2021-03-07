from collections import defaultdict

N = int(input())
tri = {}
for i in range(N):
    tri[i] = list(map(int, input().split(' ')))

dp = [[-1] * N for _ in range(N)]
dp[0] = tri[0]
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))