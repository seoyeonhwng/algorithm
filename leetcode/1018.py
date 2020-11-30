class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = [False] * len(A)
        answer[0], prev = (A[0] == 0), A[0]
        
        for i in range(1, len(A)):
            answer[i] = ((prev * 2 + A[i]) % 5 == 0)
            prev = prev * 2 + A[i]
        
        return answer

"""
- 왼쪽으로 shift = 2를 곱한다
"""