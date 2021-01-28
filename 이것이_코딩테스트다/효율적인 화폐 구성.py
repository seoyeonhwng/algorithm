import sys

N, M = map(int, input().split(' '))
money = []
for _ in range(N):
    money.append(int(input()))

# dp : 가치의 합이 i일때 최소 화폐 개수
dp = [sys.maxsize] * (M + 1)
dp[0] = 0

for i in range(1, M+1):
    for m in money:
        if i - m < 0:
            continue
        dp[i] = min(dp[i], dp[i-m] + 1)

print(-1) if dp[M] == sys.maxsize else print(dp[M])