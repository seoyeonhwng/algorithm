class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        max_len = 0
        for key, count in counter.items():
            if key-1 in counter:
                max_len = max(max_len, count + counter[key-1])
            if key+1 in counter:
                max_len = max(max_len, count + counter[key+1])
        return max_len