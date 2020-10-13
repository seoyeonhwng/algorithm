class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        
        for i in range(n):
            answer = answer ^ (start + 2 * i)
        
        return answer

"""
- 보자마자 reduce가 떠오르긴 함..
- reduce를 사용하기 위해
    1) 함수 정의 : lambda x, y : x^y
    2) iterator : nums 리스트를 생성해줌

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        
        return reduce(lambda x, y: x^y, nums)
"""