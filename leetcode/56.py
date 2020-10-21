class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        for i in sorted(intervals, key=lambda x:x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
                
        return merged
       
"""
* 콤마를 적어주면 중첩 리스트로 만들어준다! 
  - 대괄호 []를 부여한 것과 동일한 역할!
"""