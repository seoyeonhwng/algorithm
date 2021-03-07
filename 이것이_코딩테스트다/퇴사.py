N = int(input())
info = [list(map(int, input().split(' '))) for _ in range(N)]

dp = [0] * (N+1)
max_value = 0

for i in range(N-1, -1, -1):
    time = i + info[i][0]
    if time <= N:
        dp[i] = max(info[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)