from collections import defaultdict, deque
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    heap = [(0, 1)]
    dist = [sys.maxsize] * (N+1)
    dist[1] = 0

    while heap:
        count, node = heapq.heappop(heap)
        if dist[node] != count: # 이미 최단 경로를 구한 노드에 대해서만!
            continue
        
        path.append(node)

        for w, wc in graph[node]:
            if dist[w] > count + wc:
                heapq.heappush(heap, (count + wc, w))
                dist[w] = count + wc
                prev[w] = node


N, M = map(int, input().split(' '))
graph = defaultdict(list)
edges = {}

for i in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

    key = (a, b) if a < b else (b, a)
    edges[key] = i

prev = [0] * (N+1)
path = deque()
dijkstra()

path.popleft()
ans = []
for p in path:
    ans.append((prev[p], p))

print(len(ans))
for a in ans:
    print(*a)