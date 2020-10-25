class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MASK = 0x7FFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        # 음수 처리
        if a > INT_MASK:
            a = ~(a ^ MASK)
            
        return a