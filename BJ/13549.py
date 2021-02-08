from collections import defaultdict
import heapq

N, K = map(int, input().split(' '))

# N부터 K까지 최단 거리 + 걷는 것과 순간이동의 가중치가 다름 -> 다익스트라
heap = [(0, N)]
dist = defaultdict(int)

while heap:
    cost, node = heapq.heappop(heap)
    if node == K:
        print(cost)
        break

    if node in dist:
        continue

    dist[node] = cost
    for w, wc in [(node+1, 1), (node-1, 1), (node*2, 0)]:
        if 0 <= w <= 100000:
            heapq.heappush(heap, (cost + wc, w))