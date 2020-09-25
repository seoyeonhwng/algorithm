class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # dp[i] : nums[i]를 포함한 LIS의 길이
        # 나보다 크기가 작은 dp들 중에서 max에 +1
        dp = collections.defaultdict(int)
        dp[0] = 1
        answer = 1
        
        for i in range(1, len(nums)):
            max_value = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j])
            dp[i] = max_value + 1
            answer = max(answer, dp[i])
        
        return answer