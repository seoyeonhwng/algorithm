from collections import defaultdict
import heapq

N, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

# 1번 노드를 시작점으로 다익스트라 
dist = defaultdict(int)
heap = [(0, 1)]
while heap:
    count, node = heapq.heappop(heap)
    if node in dist:
        continue

    dist[node] = count
    for w in graph[node]:
        heapq.heappush(heap, (count + 1, w))

max_val = max(dist.values())
ans = []
for i in range(1, N+1):
    if dist[i] == max_val:
        ans.append(i)
print(f'{min(ans)} {dist[ans[0]]} {len(ans)}')