from collections import defaultdict
import sys
import heapq

def dijkstra(start):
    heap = [(0, start)]
    dist = defaultdict(int)

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue

        dist[node] = cost
        for w, wc in graph[node]:
            heapq.heappush(heap, (cost + wc, w))
    return dist

input = sys.stdin.readline
N, E = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split(' '))

# 1부터 N까지 최단 거리 + 가중치 
# v1, v2를 반드시 지나야함
# 1~v1, v2 ~ v1, v2 ~ N 의 최소 -> 1, v1, N 다익스트라 3번
dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(N)

poss1 = dist1.get(v1, sys.maxsize) + dist2.get(v2, sys.maxsize) + dist3.get(v2, sys.maxsize)
poss2 = dist1.get(v2, sys.maxsize) + dist2.get(v2, sys.maxsize) + dist3.get(v1, sys.maxsize)
print(-1) if poss1 >= sys.maxsize and poss2 >= sys.maxsize else print(min(poss1, poss2))
