class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        count = 0
        s = 0
        target = sum(A) // 3
        
        for a in A:
            s += a
            if s == target:
                count += 1
                s = 0
        
        return count >= 3