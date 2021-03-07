N, K = map(int, input().split(' '))
cost = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

# 순서만 다른 것은 같은 경우이므로 동전 하나에 대해서 쭉 계산 !!
for c in cost:
    for i in range(1, K+1):
        if i - c >= 0:
            dp[i] += dp[i-c]
print(dp[K])