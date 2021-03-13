N, K = map(int, input().split(' '))
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

ans = 0
for c in coins:
    q, r = divmod(K, c)
    ans += q
    K = r
print(ans)