class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                answer += 1
                
        return answer

"""
[빠른 풀이]
- 리스트 컴프리핸션!!!!

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for x in nums if len(str(x)) % 2 == 0])
"""