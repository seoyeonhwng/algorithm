class Solution:
    def numSquares(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[1] = 1
        
        square = 1
        for i in range(2, n + 1):
            if (square + 1) ** 2 <= i:
                square += 1
            
            if square ** 2 == i:
                dp[i] = 1
            else:
                # 가능한 comb 중에 최소
                combination = []
                min_value = sys.maxsize
                for j in range(1, square + 1):
                    min_value = min(min_value, dp[j * j] + dp[i - j * j])
                dp[i] = min_value
        
        return dp[n]
                    