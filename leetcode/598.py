class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
      
        for i in range(1, len(ops)):
            x1, y1 = ops[i - 1]
            x2, y2 = ops[i]
            ops[i] = [min(x1, x2), min(y1, y2)]
            
        return ops[-1][0] * ops[-1][1]