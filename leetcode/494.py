class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp : key를 계산 결과, value를 개수
        dp = collections.defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        
        for i in range(1, len(nums)):
            tmp = collections.defaultdict(int)
            for k, v in dp.items():
                tmp[k + nums[i]] += v
                tmp[k - nums[i]] += v
            dp = tmp
                
        return dp[S]