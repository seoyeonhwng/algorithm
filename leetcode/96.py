class Solution:
    def numTrees(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1

        # 가능한 왼쪽 자식 수, 오른쪽 자식 수 조합을 구한뒤 곱해서 다 더한다!
        for i in range(1, n+1):
            for j in range(i): 
                dp[i] += dp[j] * dp[i-j-1]
                
        return dp[n]