from collections import defaultdict
import heapq

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
start, end = map(int, input().split(' '))

heap = [(0, start, [start])]
dist = {}

while heap:
    cost, node, path = heapq.heappop(heap)
    if node in dist:
        continue

    dist[node] = (cost, path)
    for w, wc in graph[node]:
        heapq.heappush(heap, (cost + wc, w, path + [w]))

print(dist[end][0])
print(len(dist[end][1]))
print(*dist[end][1])