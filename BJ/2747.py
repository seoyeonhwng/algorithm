N = int(input())

# dp : n번째 피보나치 수를 저장
dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])