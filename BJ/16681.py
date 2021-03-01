from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = [(0, start)]
    dist = defaultdict(int)

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue

        dist[node] = cost
        for w, wc in graph[node]:
            if heights[node] < heights[w]:
                heapq.heappush(heap, (cost + wc, w))

    return dist

N, M, D, E = map(int, input().split(' '))
heights = [-1] + list(map(int, input().split(' ')))
graph = defaultdict(list)
for _ in range(M):
    a, b, n = map(int, input().split(' '))
    graph[a].append((b, n))
    graph[b].append((a, n))

# 집과 고대에서 임의의 지점까지의 최단 거리
dist1 = dijkstra(1)
dist2 = dijkstra(N)

ans = -sys.maxsize
for i in range(2, N):
    if not dist1.get(i) or not dist2.get(i):
        continue
    value = (heights[i] * E) - ((dist1[i] + dist2[i]) * D)
    ans = max(ans, value)
print('Impossible') if ans == -sys.maxsize else print(ans)