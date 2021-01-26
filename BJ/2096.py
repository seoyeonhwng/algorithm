N = int(input())
max_dp, min_dp = [], []

for _ in range(N):
    nums = list(map(int, input().split(' ')))
    if not max_dp:
        max_dp = nums
        min_dp = nums
        continue
    
    max_ndp = [0] * 3
    min_ndp = [0] * 3
    for i in range(3):
        if i == 0:
            max_ndp[i] = nums[i] + max(max_dp[0], max_dp[1])
            min_ndp[i] = nums[i] + min(min_dp[0], min_dp[1])
        elif i == 1:
            max_ndp[i] = nums[i] + max(max_dp)
            min_ndp[i] = nums[i] + min(min_dp)
        else:
            max_ndp[i] = nums[i] + max(max_dp[1], max_dp[2])
            min_ndp[i] = nums[i] + min(min_dp[1], min_dp[2])
    max_dp, min_dp = max_ndp, min_ndp
    
print(max(max_dp), min(min_dp))

