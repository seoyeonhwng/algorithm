from collections import defaultdict
import heapq

# 1부터 각 노드까지 k번째 최단 거리를 구함 -> 다익스트라

N, M, K = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))

info = [[K, -1] for _ in range(N + 1)]
heap = [(0, 1)]
while heap:
    cost, node = heapq.heappop(heap)
    if info[node][0] == 0:
        continue

    info[node][0] -= 1
    info[node][1] = cost
    for w, wc in graph[node]:
        heapq.heappush(heap, (cost + wc, w))

for i in range(1, N+1):
    k, cost = info[i]
    print(cost) if k == 0 else print(-1)