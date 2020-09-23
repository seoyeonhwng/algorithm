class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = [False] * (len(nums) - 1)
        
        for n in nums:
            if check[n - 1]:
                return n
            check[n - 1] = True

"""
빠른 풀이
- 시간 복잡도 O(n), 공간 복잡도 O(1) 플이
- 러너 기법 (slower는 한칸씩, faster는 두칸씩 이동)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 두 러너가 만나는 지점을 찾는다!
        slower = faster = nums[0]
        while True:
            slower = nums[slower]
            faster = nums[nums[faster]]
            if slower == faster:
                break
                
        # 사이클의 시작 = 중복된 원소를 찾는다
        slower = nums[0]
        while slower != faster:
            slower = nums[slower]
            faster = nums[faster]
        
        return faster
"""