class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        left, right = 0, 0
        
        for c in s:
            if c == 'R':
                right += 1
            else:
                left += 1
                
            if left == right:
                answer += 1
                
        return answer
            