class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def get_pos(n):
            # None이 아닌 n번째 위치 리턴
            count = 0
            for i, v in enumerate(answer):
                if v is None:
                    if count == n:
                        return i
                    count += 1
            return len(answer)-1
        
        heap = []
        for height, cnt in people:
            heapq.heappush(heap, (height, -cnt))
        
        answer = [None] * len(people)
        while heap:
            h, c = heapq.heappop(heap)
            pos = get_pos(-c)
            answer[pos] = [h, -c]
        return answer
            

"""
[빠른 풀이]
- 키가 큰 사람부터 삽입!!!!

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
"""