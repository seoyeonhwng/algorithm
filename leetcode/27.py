# 삭제할 원소를 맨 뒤로 몰아넣고, 배열의 크기를 줄인다!
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
                
        return n