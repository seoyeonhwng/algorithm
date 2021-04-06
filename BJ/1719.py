from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def dijstra(start):
    dist[start] = 0
    prev[start] = '-'

    heap = [(0, start)]
    while heap:
        count, node = heapq.heappop(heap)
        if dist[node] != count:
            continue

        for w, wc in graph[node]:
            if dist[w] > count + wc:
                dist[w] = count + wc
                prev[w] = node + 1
                heapq.heappush(heap, (count + wc, w))
        


N, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

answer = []
for node in range(N):
    dist = [sys.maxsize] * N
    prev = [sys.maxsize] * N
    dijstra(node)

    answer.append(prev)

for col in zip(*answer):
    print(*col)