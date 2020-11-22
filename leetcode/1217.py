class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 짝수끼리 홀수끼리 이동은 공짜!
        odd, even = 0, 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
       
        return min(even, odd)