import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    # start에서 다른 노드까지의 최단 거리
    heap = [(0, start)]
    dist = [sys.maxsize] * (N+1)
    dist[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        
        for w, wc in graph[node]:
            if dist[w] > cost + wc:
                heapq.heappush(heap, (cost + wc, w))
                dist[w] = cost + wc
            
    return dist

N = int(input())
graph = defaultdict(list)
for i in range(N):
    tmp = list(map(int, input().rstrip().split(' ')))
    for j, c in enumerate(tmp):
        if c == 0:
            continue
        graph[i].append((j, c))

P, Q = map(int, input().rstrip().split(' '))
t_list = [list(map(int, input().rstrip().split(' '))) for _ in range(P)]
h_list = [list(map(int, input().rstrip().split(' '))) for _ in range(Q)]
a_list, b_list = (t_list, h_list) if P < Q else (h_list, t_list)

ans = -sys.maxsize
for t, tw in a_list:
    dist = dijkstra(t-1)
    for h, hw in b_list:
        ans = max(ans, (tw + hw) - dist[h-1])
print(ans)
