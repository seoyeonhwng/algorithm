class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        target = sum(nums) // 2
        heap, answer = [], []
        for n in nums:
            heapq.heappush(heap, -n)
        
        # 조건을 만족할때까지 배열에서 가장 큰 값을 더해감 (greedy)
        while sum(answer) <= target:
            answer.append(-heapq.heappop(heap))
        return answer