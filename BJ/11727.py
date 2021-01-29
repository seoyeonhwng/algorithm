import sys

N = int(input())
if N == 1:
    print(1)
    sys.exit()

# dp : n일때 필요한 타일의 수
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[N] % 10007)