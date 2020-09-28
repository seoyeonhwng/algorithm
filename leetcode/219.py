class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = collections.defaultdict(int)
        
        for i, n in enumerate(nums):
            if n in idx and i - idx.get(n) <= k:
                return True
            idx[n] = i
        
        