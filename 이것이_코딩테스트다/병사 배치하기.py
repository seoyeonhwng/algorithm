N = int(input())
nums = list(map(int, input().split(' ')))
nums.reverse()

# 전체 길이 - 가장 긴 증가하는 수열의 길이
dp = [1] * N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))