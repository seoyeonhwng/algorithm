import sys
import heapq
from collections import defaultdict

def dijkstra(start):
    distance = [sys.maxsize] * (N+1)
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        if distance[node] < cost:
            continue

        for w, wc in graph[node]:
            new_cost = cost + wc
            if new_cost < distance[w]:
                distance[w] = new_cost
                heapq.heappush(heap, (new_cost, w))
    return distance

# 모든 정점에서 다익스트라를 실행
N, M, X = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append((b, c))

# N짜리 거리 배열 선언
result = []
for i in range(1, N+1):
    result.append(dijkstra(i))

ans = -sys.maxsize
for i in range(N):
    ans = max(ans, result[i][X] + result[X-1][i+1])
print(ans)