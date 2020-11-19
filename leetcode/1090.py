class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        # 각 단계에서 가장 큰 values의 원소를 선택
        answer, counter = 0, collections.defaultdict(int)
        heap = []
        for v, l in zip(values, labels):
            heapq.heappush(heap, (-v, l))
        
        while num_wanted > 0 and heap:
            candi, label = heapq.heappop(heap) # largest
            if counter[label] < use_limit:
                counter[label] += 1
                answer, num_wanted = answer - candi, num_wanted - 1
        return answer
        