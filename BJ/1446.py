from collections import defaultdict
import heapq, sys

def dijsktra(): # 0부터 D까지 최단 거리
    heap = [(0, 0)]
    dist = [sys.maxsize] * (1001)
    dist[0] = 0

    while heap:
        count, node = heapq.heappop(heap)
        if dist[node] != count:
            continue
        if node == D:
            return count

        candi = [(node + 1, 1)] + short[node]
        for w, wc in candi:
            if dist[w] > wc + count:
                dist[w] = wc + count
                heapq.heappush(heap, (wc + count, w))
    

N, D = map(int, input().split(' '))
short = defaultdict(list)
for _ in range(N):
    f, t, w = map(int, input().split(' '))
    short[f].append((t, w))

print(dijsktra())