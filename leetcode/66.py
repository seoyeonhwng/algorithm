class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p1 = len(digits) - 1
        res, carry = [], 0
        
        while p1 >= 0:
            x1 = digits[p1] if p1 >= 0 else 0
            x2 = 1 if p1 == len(digits)-1 else 0
            
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
        
        if carry:
            res.append(carry)
        
        return res[::-1]
        