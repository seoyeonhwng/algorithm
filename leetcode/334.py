class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # dp[i] : nums[i]를 포함해서 만들 수 있는 increasing subsequence
        dp = collections.defaultdict(int)
        dp[0] = 1
        
        for i in range(1, len(nums)):
            max_value = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j])
            dp[i] = max_value + 1
            if dp[i] == 3:
                return True
        
        return False

"""
[빠른 풀이]
- 가장 작은 원소, 두번째로 작은 원소를 찾고 가장 작은 원소, 두번째로 작은 원소를 찾고

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = sys.maxsize
        second = sys.maxsize
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else: # 두 수보다 큰 숫자가 존재!
                return True
        
        return False
"""