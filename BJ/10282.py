from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def dijkstra():
    heap = [(0, C)]
    while heap:
        count, node = heapq.heappop(heap)

        if dist[node] != count:
            continue

        for w, wc in graph[node]:
            if dist[w] > count + wc:
                dist[w] = count + wc
                heapq.heappush(heap, (count + wc, w))

for _ in range(int(input())):
    N, D, C = map(int, input().split(' '))
    graph = defaultdict(list)
    for _ in range(D):
        a, b, s = map(int, input().split(' '))
        graph[b].append((a, s))

    dist = [sys.maxsize] * (N + 1)
    dist[C] = 0
    dijkstra()

    ans_count, ans = 0, 0
    for i in range(1, N+1):
        if dist[i] == sys.maxsize:
            continue

        ans_count += 1
        ans = max(ans, dist[i])
    print(f'{ans_count} {ans}')