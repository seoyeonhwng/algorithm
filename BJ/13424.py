import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue

        dist[node] = cost
        for w, wc in graph[node]:
            heapq.heappush(heap, (cost + wc, w))

    dist[start] = 0

for _ in range(int(input())):
    # 다익스트라 N번!
    N, M = map(int, input().split(' '))
    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split(' '))
        graph[a].append((b, c))
        graph[b].append((a, c))
    K = int(input())
    friends = list(map(int, input().split(' ')))

    ans, ans_idx = sys.maxsize, 0
    for i in range(1, N+1):
        dist, total = defaultdict(int), 0
        dijkstra(i)
        for f in friends: # i에서 f까지 최단거리 합
            total += dist[f]

        if total < ans:
            ans = total
            ans_idx = i
    print(ans_idx)
