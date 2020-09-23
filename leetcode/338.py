class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        
        n = 0
        while 2 ** n <= num:
            n += 1
            
        dp = collections.defaultdict(list)
        dp[1] = [0, 1]
        dp[2] = [1, 2]
        
        for i in range(3, n+1):
            for e in dp[i - 1]:
                dp[i].append(e)
                dp[i].append(e + 1)
        
        # dp n-1까지는 모두 더하고
        # dp[n]의 num % 2 ** n 까지
        print(n, dp)
        answer = []
        for i in range(1, n):
            answer += dp[i]
        index = num % (2 ** (n - 1))
        answer += dp[n][:index+1]
        
        return answer

"""
[빠른 풀이]
- 홀수인 경우, 앞 숫자의 1 개수 + 1
- 짝수인 경우, 절반 숫자의 1 개수

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i // 2])
        return dp
"""
            