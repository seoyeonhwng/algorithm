for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(1)
        continue
    if N == 2:
        print(2)
        continue
    if N == 3:
        print(4)
        continue

    dp = [0] * (N+1) # i를 1,2,3의 합으로 나타내는 경우의 수
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])