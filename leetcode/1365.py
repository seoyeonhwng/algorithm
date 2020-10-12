class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for i in range(len(nums)):
            sub = nums[:i] + nums[i+1:]
            sub.sort()
            count.append(bisect.bisect_left(sub, nums[i]))
        
        return count

"""
[빠른 풀이]
- 정렬한 배열의 인덱스가 해당 원소보다 작은 원소의 개수임을 이용!!!!

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        index = {}
        
        for i, n in enumerate(sorted_nums):
            if n not in index:
                index[n] = i
                
        answer = []
        for n in nums:
            answer.append(index[n])
        return answer
"""