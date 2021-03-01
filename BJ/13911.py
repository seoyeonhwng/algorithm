from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def dijkstra(heap, dist):
    while heap:
        count, node = heapq.heappop(heap)
        if dist[node] != count:
            continue
       
        for w, wc in graph[node]:
            if dist[w] > count + wc:
                heapq.heappush(heap, (count + wc, w))
                dist[w] = count + wc
    return dist


V, E = map(int, input().rstrip().split(' '))
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().rstrip().split(' '))
    graph[u].append((v, w))
    graph[v].append((u, w))
M, X = map(int, input().rstrip().split(' '))
m_list = list(map(int, input().rstrip().split(' ')))
S, Y = map(int, input().rstrip().split(' '))
s_list = list(map(int, input().rstrip().split(' ')))

# 맥도날드로 다익스트라
m_heap = []
m_dist = [sys.maxsize] * (V+1)
for m in m_list:
    m_heap.append((0, m))
    m_dist[m] = 0
m_dist = dijkstra(m_heap, m_dist)

# 스타벅스로 다익스트라
s_heap = []
s_dist = [sys.maxsize] * (V+1)
for s in s_list:
    s_heap.append((0, s))
    s_dist[s] = 0
s_dist = dijkstra(s_heap, s_dist)

ans = sys.maxsize
for node in range(1, V+1):
    if node in m_list or node in s_list:
        continue
    if m_dist[node] > X or s_dist[node] > Y:
        continue
    ans = min(ans, m_dist[node] + s_dist[node])
print(-1) if ans == sys.maxsize else print(ans)