from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    heap = [(0, start)]
    dist[start] = 0

    while heap:
        count, node = heapq.heappop(heap)
        if dist[node] != count:
            continue

        for w, wc in graph[node]:
            if dist[w] > wc + count:
                heapq.heappush(heap, (wc + count, w))
                dist[w] = wc + count

N, M, R = map(int, input().split(' '))
items = list(map(int, input().split(' ')))
graph = defaultdict(list)
for _ in range(R):
    a, b, s = map(int, input().split(' '))
    graph[a].append((b, s))
    graph[b].append((a, s))

# 다익스트라 N번
ans = 0
for i in range(1, N+1):
    dist = [sys.maxsize] * (N+1)
    dijkstra(i)

    # M보다 dist값이 작으면 해당 item[j] 얻을 수 있음
    total = 0
    for j in range(1, N+1):
        if dist[j] <= M:
            total += items[j-1]
    ans = max(ans, total)
print(ans)