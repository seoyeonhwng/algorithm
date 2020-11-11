class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        
        return (-first-1) * (-second-1)