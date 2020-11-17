class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        counter = collections.Counter(arr)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))
            
        count, answer = 0, 0
        while count < half:
            count += -(heapq.heappop(heap)[0])
            answer += 1
        return answer

"""
[빠른 풀이]
- counter.values()를 정렬한다!
- 원소의 개수 셀 필요없이 index + 1로 처리

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        occur = sorted(collections.Counter(arr).values(), reverse=True)
        
        total = 0
        for index, count in enumerate(occur):
            total += count
            if total >= half:
                return index + 1
        return len(occur)
"""