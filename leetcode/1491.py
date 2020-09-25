class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        max_s = -sys.maxsize
        min_s = sys.maxsize
        
        for s in salary:
            total += s
            max_s = max(max_s, s)
            min_s = min(min_s, s)
            
        total = total - max_s - min_s
        return total / (len(salary) - 2)

"""
[빠른 풀이]
- mean(list)도 가능!

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return mean(salary[1:-1])
"""