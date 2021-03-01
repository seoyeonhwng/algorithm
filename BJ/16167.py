from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def get_cost(c, d, e):
    if e <= 10:
        return c
    return c + (e - 10) * d

def dijkstra():
    heap = [(0, 1, 1)]
    dist = defaultdict(list)

    while heap:
        cost, count, node = heapq.heappop(heap)
        if node in dist:
            continue

        dist[node] = [cost, count]
        for w, wc in graph[node]:
            heapq.heappush(heap, (cost + wc, count + 1, w))
    return dist

N, R = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(R):
    a, b, c, d, e = map(int, input().split(' '))
    cost = get_cost(c, d, e)
    graph[a].append((b, cost))

dist = dijkstra()
print('It is not a great way.') if not dist.get(N) else print(*dist.get(N))