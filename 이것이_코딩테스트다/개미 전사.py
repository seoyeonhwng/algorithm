N = int(input())
food = list(map(int, input().split(' ')))

# dp = 각 식량창고까지 선택했을때의 최대값
dp = [0] * N
dp[0] = food[0]
dp[1] = max(food[0], food[1]) # 이부분 놓치지 말자!!!

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + food[i])

print(dp[N-1])