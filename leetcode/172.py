class Solution:
    def trailingZeroes(self, n: int) -> int:
        # trailing zero는 5의 개수로 결정된다!
        count = 0
        
        while n:
            count += n // 5
            n = n // 5
            
        return count