class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap = []
        for i, a in enumerate(A):
            heapq.heappush(heap, (a, i))
            
        for _ in range(K):
            v, i = heapq.heappop(heap)
            heapq.heappush(heap, (-v, i))
            A[i] = -A[i]
        return sum(A)

"""
- sum의 최대를 찾기 위해 각 단계마다 min값을 타겟으로 선택한다 -> greedy
"""