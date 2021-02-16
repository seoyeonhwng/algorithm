from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, S)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue

        dist[node] = cost
        for w, wc in graph[node]:
            heapq.heappush(heap, (cost + wc, w))

for _ in range(int(input())):
    N, M, T = map(int, input().split(' '))
    S, G, H = map(int, input().split(' '))
    graph = defaultdict(list)
    edges = defaultdict(int)

    for i in range(M):
        a, b, c = map(int, input().split(' '))
        if (G == a and H == b) or (G == b and H == a):
            weight = 2 * c -1 
        else:
            weight = 2 * c
        graph[a].append((b, weight))
        graph[b].append((a, weight))
        
    candi = [int(input()) for _ in range(T)]
    dist = defaultdict(int)
    dijkstra()

    ans = []
    for c in candi:
        if dist[c] % 2 == 1: # (g-h)를 지나온 것!
            ans.append(c)
    print(*sorted(ans))

"""
* 다익스트라는 최단 거리를 보장해줌
* 하지만 만약 최단 거리가 여러개라면 path를 다 검사해야함 
* 내가 원하는 간선은 홀수로, 나머지는 짝수로 만들어줘서 최단 거리 합으로 해당 간선을 지나왔는지 체크!!
"""