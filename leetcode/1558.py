class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def check(arr):
            for a in arr:
                if a > 1:
                    return False
            return True
        
        count = 0
        while not check(nums):
            count += sum([n % 2 for n in nums]) + 1
            nums = [n // 2 for n in nums]

        return count + sum(nums)