N, K = map(int, input().split(' '))
info = [list(map(int, input().split(' '))) for _ in range(N)]

# 쪼갤수 없는 배낭 문제 -> dp
# dp[i][j] : i개의 배낭을 사용해서 최대 무게 j일때 최고 가치합

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = info[i-1]
    for j in range(K+1):
        if j < w:
            dp[i][j] = dp[i-1][j] # 해당 배낭 사용안하는 경우
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])