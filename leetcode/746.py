class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-1], dp[-2])

"""
* dp문제는 아래 순서로 푼다!
1. dp에 어떤 값을 저장할지
2. dp[0], dp[1] 정의
3. dp 점화식 정의
"""