class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def check(inter1, inter2):
            return inter1[0] >= inter2[0] and inter1[1] <= inter2[1]
        
        intervals = sorted(intervals, key=lambda x:x[0], reverse=True)
        count = len(intervals)
        
        for i in range(len(intervals)):
            result = [check(intervals[i], intervals[j]) for j in range(i+1, len(intervals))]
            if any(result):
                count -= 1
        
        return count
            
            
"""
[빠른 풀이]
- 뒤에 있는 변수들을 다 비교하지 않기 위해 ending이라는 변수를 사용
- 비교를 최소화하자!!!!!!!!!

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        res, ending = 0, 0
        for _, end in intervals:
            if end > ending:
                res += 1
                ending = end
        return res
"""