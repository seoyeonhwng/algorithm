# 합의 최대 -> dp
N = int(input())
cost = list(map(int, input().split(' ')))

dp = [0] * (N+1) # 카드 i개를 구매하기 위해 지불하는 최댓값
for i in range(1, N+1):
    dp[i] = cost[i-1]

for i in range(2, N+1):
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[N])