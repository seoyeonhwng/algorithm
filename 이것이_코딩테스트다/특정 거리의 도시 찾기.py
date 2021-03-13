from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(X, 0)])

    while queue:
        node, count = queue.popleft()

        for w in graph[node]:
            if dist[w] > count + 1:
                dist[w] = count + 1
                queue.append((w, count + 1))

N, M, K, X = map(int, input().rstrip().split(' '))
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split(' '))
    graph[u].append(v)

dist = [sys.maxsize] * (N+1)
dist[X] = 0
bfs()

ans = 0
for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        ans += 1
if ans == 0:
    print(-1)