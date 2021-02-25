import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    # start에서 다른 노드까지의 최단 거리
    heap = [(0, start)]
    dist = defaultdict(int)

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue
        
        dist[node] = cost
        for w, wc in graph[node]:
            heapq.heappush(heap, (cost + wc, w))
    return dist

N = int(input())
graph = defaultdict(list)
for i in range(N):
    tmp = list(map(int, input().split(' ')))
    for j, c in enumerate(tmp):
        if c == 0:
            continue
        graph[i].append((j, c))

P, Q = map(int, input().split(' '))
t_list = []
for _ in range(P):
    a, b = map(int, input().split(' '))
    t_list.append((a, b))
h_list = []
for _ in range(Q):
    a, b = map(int, input().split(' '))
    h_list.append((a, b))

ans = -sys.maxsize
for t, tw in t_list:
    dist = dijkstra(t-1)
    for h, hw in h_list:
        ans = max(ans, (tw + hw) - dist[h-1])
print(ans)
