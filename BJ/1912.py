N = int(input())
nums = list(map(int, input().split(' ')))

# dp[i] : nums[i]를 포함했을때 가장 큰 합
dp = [0] * N
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))