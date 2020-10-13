class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        
        for i, n in zip(index, nums):
            target.insert(i, n)
        return target

"""
[빠른 풀이]
- list에서 insert는 O(n)이므로 insert대신 슬라이싱을 이용하면 조금 더 빠르다!

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        
        for i, n in zip(index, nums):
            if i == len(target):
                target.append(n)
            else:
                target = target[:i] + [n] + target[i:]
            
        return target
"""