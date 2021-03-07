N = int(input())

# 배치하는 문제 (경우의 수) -> dp!!
# 점화식 : 2 * dp[i-1] + dp[i-2]
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 3
for i in range(2, N+1):
    dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901
print(dp[N])