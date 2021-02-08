import sys
from collections import defaultdict
import heapq


# A부터 B까지 최단거리 + 가중치 -> 다익스트라
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
start, end = map(int, input().split())

heap = [(0, start)]
dist = defaultdict(int)

while heap:
    cost, node = heapq.heappop(heap)
    if node in dist:
        continue

    dist[node] = cost
    for w, wc in graph[node]:
        heapq.heappush(heap, (cost + wc, w))
print(dist[end])