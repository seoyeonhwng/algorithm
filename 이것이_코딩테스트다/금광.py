import sys

for _ in range(int(input())):
    N, M = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))

    gold = [[0] * M for _ in range(N)]
    gold[0][0] = nums[0]
    for n in range(1, N * M):
        i, j = divmod(n, M)
        gold[i][j] = nums[n]

    # dp[i][j] : (i, j)에서의 최대 이익
    dp = [[0] * M for _ in range(N)]
    for i in range(N):
        dp[i][0] = gold[i][0]

    for j in range(1, M):
        for i in range(N):
            dp[i][j] = gold[i][j] + dp[i][j-1]
            if i-1 >= 0:
                dp[i][j] = max(dp[i][j], gold[i][j] + dp[i-1][j-1])
            if i+1 < N:
                dp[i][j] = max(dp[i][j], gold[i][j] + dp[i+1][j-1])

    ans = -sys.maxsize
    for row in dp:
        ans = max(ans, row[-1])
    print(ans)
