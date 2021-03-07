N = int(input())
dp = [[0] * 10 for _ in range(N)]
dp[0] = [1] * 10

for i in range(1, N):
    val = 0
    for j in range(10):
        val += dp[i-1][j]
        dp[i][j] = val % 10007
        
print(sum(dp[N-1]) % 10007)