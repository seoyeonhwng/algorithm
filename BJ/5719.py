from collections import defaultdict, deque
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, S)]
    dist = [sys.maxsize] * N
    dist[S] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        for w, wc in graph[node]:
            if dist[w] > wc + cost and (not removed[node][w]):
                dist[w] = wc + cost
                heapq.heappush(heap, (wc + cost, w))
    return dist

# 최단 거리를 알때 지나간 간선 아는 법!
def remove_edges(dist):
    queue = deque([D])

    while queue:
        node = queue.popleft()
        for bef, cost in graph_r[node]:
            if dist[node] == dist[bef] + cost and (not removed[bef][node]):
                removed[bef][node] = 1
                queue.append(bef)


while True:
    N, M = map(int, input().split(' '))
    if N == 0 and M == 0:
        break
    
    S, D = map(int, input().split(' '))
    graph = defaultdict(list)
    graph_r = defaultdict(list)
    for i in range(M):
        u, v, p = map(int, input().split(' '))
        graph[u].append((v, p))
        graph_r[v].append((u, p))

    removed = [[0] * N for _ in range(N)]
    dist = dijkstra()
    remove_edges(dist)
    
    dist = dijkstra()
    print(-1) if dist[D] == sys.maxsize else print(dist[D])