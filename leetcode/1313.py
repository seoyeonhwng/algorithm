class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(nums) // 2):
            answer += [nums[2*i + 1] for _ in range(nums[2*i])]
        
        return answer