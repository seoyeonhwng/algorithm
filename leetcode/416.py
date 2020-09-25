class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # 합이 target인 배열을 찾는다
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i - n]
                
        return dp[target]
        
        