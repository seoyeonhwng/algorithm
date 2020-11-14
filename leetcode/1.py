class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 인덱스가 필요하니까 값를 키로 하는 딕셔너리를 만든다
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return i, nums_map[target-num]