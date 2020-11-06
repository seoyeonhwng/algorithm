class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # 값의 비교를 이 mid가 아니고 진짜 mid를 찾아서 비교한다
            
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
            
        return -1