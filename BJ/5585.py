N = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

# 거스름돈의 개수가 가장 작게 = 큰 동전부터 거슬러준다 -> 그리디
ans = 0
for c in coins:
    q, r = divmod(N, c)
    ans += q
    N = r
print(ans)

