class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = {}
        for i, c in zip(indices, s):
            string[i] = c
            
        shuffled = sorted(string.items(), key=lambda x: (x[0], x[1]))
        return ''.join([s[1] for s in shuffled])
            
"""
[빠른 풀이]
- 정렬하는 것보다 인덱스로 접근하는것이 더 빠르니까..!

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = [None] * len(s)
        
        for i, c in enumerate(s):
            string[indices[i]] = c
        return ''.join(string)
"""