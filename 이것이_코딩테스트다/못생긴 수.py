# 못생긴 수에 2, 3, 5를 곱하면 못생긴 수
# 못생긴 수를 작은 순서대로 하나씩 찾아감

N = int(input())
dp = [0] * N
dp[0] = 1

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

for i in range(1, N):
    # 못생긴 수 후보들 중에 최소
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    elif dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    else:
        i5 += 1
        next5 = dp[i5] * 5
print(dp[N-1])