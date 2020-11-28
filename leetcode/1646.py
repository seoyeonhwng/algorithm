class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        dp = collections.defaultdict(int)
        dp[0] = 0
        dp[1] = 1
        max_value = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + dp[i // 2 + 1]
            max_value = max(max_value, dp[i])
        
        return max_value