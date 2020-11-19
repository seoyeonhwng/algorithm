class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        left, right = 0, 0
        answer = 0
        
        while left < len(s):
            # expand right pointer
            while right < len(s) and s[left] == s[right]:
                right += 1
            
            tmp = cost[left:right]
            answer += (sum(tmp) - max(tmp)) if len(tmp) > 1 else 0
            left, right = right, right + 1
        
        return answer
            
"""
[빠른 풀이]
- 연속된 문자열에 한하여 축적합과 그 중 max값을 유지한다!

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        answer, cur_sum, cur_max = 0, cost[0], cost[0]
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cur_sum, cur_max = cur_sum + cost[i], max(cur_max, cost[i])
            else:
                answer = answer + cur_sum - cur_max
                cur_sum, cur_max = cost[i], cost[i]
        return answer + cur_sum - cur_max
            
            
            
"""