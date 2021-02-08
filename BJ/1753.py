import heapq
from collections import defaultdict
import sys

# 시작점에서 다른 모든 정점으로의 최단 거리 -> 다익스트라!!
input = sys.stdin.readline
V, E = map(int, input().split(' '))
start = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

dist = defaultdict(int)
heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)
    if node in dist:
        continue
    
    dist[node] = cost
    for w, wc in graph[node]:
        heapq.heappush(heap, (cost + wc, w))

dist[start] = 0
for i in range(1, V+1):
    print(dist[i]) if dist.get(i, -1) != -1 else print('INF')