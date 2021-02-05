from collections import defaultdict
import sys
import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [sys.maxsize] * (N + 1)
    distance[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)
        if distance[now] < cost:
            continue

        for node, dist in graph[now]:
            new_cost = cost + dist
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(heap, (new_cost, node))
    return distance

# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수 = 도시 C에서 도달 가능한지
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간 = 도시 C에서 가능한 거리 중에 최대
# 노드의 수가 30000 -> 다익스트라!!!
N, M, C = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    f, t, c = map(int, input().split(' '))
    graph[f].append((t, c))

distance = dijkstra(C) # distance 갱신

ans_count, ans_dist = -1, 0
for d in distance:
    if d == sys.maxsize:
        continue
    ans_count += 1
    ans_dist = max(ans_dist, d)
print(ans_count, ans_dist)
