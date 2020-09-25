class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        result = []
        
        for n in nums:
            s += n
            result.append(s)
            
        return result