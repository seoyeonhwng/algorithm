from collections import defaultdict, deque
import sys, heapq
input = sys.stdin.readline

def bfs():
    heap = [(0, 0, 1)]
    dist = [[sys.maxsize] * (K+1) for _ in range(N+1)]
    dist[1][0] = 0

    while heap:
        cost, k, node = heapq.heappop(heap)
        if dist[node][k] != cost:
            continue

        for w, wc in graph[node]:
            if k < K and dist[w][k+1] > cost:
                dist[w][k+1] = cost
                heapq.heappush(heap, (cost, k+1, w))

            if dist[w][k] > cost + wc:
                dist[w][k] = cost + wc
                heapq.heappush(heap, (cost + wc, k, w))

    return dist

N, M, K = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = bfs()
print(min(dist[N]))