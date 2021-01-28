import sys

N = int(input())
dp = [0] * (N + 1)

# 규칙성, 점화식을 찾는다!
# dp = n을 1로 만들기 위한 최소 횟수를 저장
for i in range(2, N+1):
    min_value = dp[i - 1] + 1
    if i % 5 == 0:
        min_value = min(min_value, dp[i // 5] + 1)
    if i % 3 == 0:
        min_value = min(min_value, dp[i // 3] + 1)
    if i % 2 == 0:
        min_value = min(min_value, dp[i // 2] + 1)
    dp[i] = min_value

print(dp[N])