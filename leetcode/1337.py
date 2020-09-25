class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i, row in enumerate(mat):
            heapq.heappush(heap, (row.count(1), i))
        
        result = []
        for _ in range(k):
            v = heapq.heappop(heap)
            result.append(v[1])
                           
        return result