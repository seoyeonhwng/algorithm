import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

if N == 1:
    print(0)
else:
    ans = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans += (a + b)
        if heap:
            heapq.heappush(heap, a + b)

    print(ans)

"""
* 해섷
- 항상 가장 작은 크기의 두 카드 묶음을 합칠때 최적의 해를 보장 -> heap!!
- 카드가 하나있을때까지 결합 과정을 반복
- N == 1로 분기 탈필요 없이 아래처럼 하면 됨

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    result += one + two
    heapq.heappush(heap, one + two)
"""