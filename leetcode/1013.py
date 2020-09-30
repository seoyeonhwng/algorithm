class Solution:
    # target sum을 구할 수 있는 것이 핵심!
    # 내가 아는 것을 최대한 알아내자
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