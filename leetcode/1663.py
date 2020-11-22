class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        answer, k = ['a'] * n, k - n
        
        for i in range(n-1, -1, -1):
            possible = min(25, k)
            answer[i] = chr(ord('a') + possible)
            k -= possible
        
        return ''.join(answer)
  
"""
- lexicographically smallest string 이니까 뒤에서부터 가장 큰 문자를 할당!!!
"""