from bisect import bisect_left
import sys, heapq
input = sys.stdin.readline

# 작은 가방부터 담을 수 있는 가장 비싼 보석을 담는다 !! => 그리디
N, K = map(int, input().rstrip().split(' '))
jew = []
for _ in range(N):
    m, v = map(int, input().rstrip().split(' '))
    heapq.heappush(jew, (m, v))

bags = []
for _ in range(K):
    bags.append(int(input().rstrip()))
bags.sort()

answer, candi = 0, []
for b in bags:
    # 가방에 담을 수 있는 보석은 빼놓음!!
    while jew and b >= jew[0][0]:
        heapq.heappush(candi, -heapq.heappop(jew)[1])
    
    if candi:
        answer += -heapq.heappop(candi)
print(answer)