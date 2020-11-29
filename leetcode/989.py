class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        k = list(str(K))
        p1 = len(A) - 1
        p2 = len(k) - 1
        carry, res = 0, []
        
        while p1 >= 0 or p2 >= 0:
            x1 = A[p1] if p1 >= 0 else 0
            x2 = int(k[p2]) if p2 >= 0 else 0
            
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            
            res.append(value)
            p1 -= 1
            p2 -= 1
            
        if carry:
            res.append(carry)
        
        return res[::-1]