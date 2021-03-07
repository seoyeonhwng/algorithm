from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, S, 1)]
    dist[S][1] = 0 # 벽부수기 스타일은 무조건 이렇게!! 모든 벽을 부수는 경우가 최소라는 보장이 없기 때문

    while heap:
        count, node, f = heapq.heappop(heap)

        for w, wc in graph[node]:
            if dist[w][f] > count + wc:
                heapq.heappush(heap, (count + wc, w, f))
                dist[w][f] = count + wc
        
        if f == 1:
            for w in flight[node]:
                if dist[w][f-1] > count:
                    heapq.heappush(heap, (count, w, f-1))
                    dist[w][f-1] = count

N, M, F, S, T = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

flight = defaultdict(list)
for _ in range(F):
    a, b = map(int, input().split(' '))
    flight[a].append(b)

dist = [[sys.maxsize] * 2 for _ in range(N)]
dijkstra()
print(min(dist[T]))
