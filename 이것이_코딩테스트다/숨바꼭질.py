from collections import deque, defaultdict
import sys

def bfs():
    queue = deque([(1, 0)])
    dist[1] = 0

    while queue:
        node, count = queue.popleft()

        for w in graph[node]:
            if dist[w] > count + 1:
                dist[w] = count + 1
                queue.append((w, count + 1))

N, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

dist = [sys.maxsize] * (N+1)
bfs()

ans, ans_dist, ans_cnt = 0, 0, 0
for i in range(1, N+1):
    if dist[i] > ans_dist:
        ans = i
        ans_dist = dist[i]
        ans_cnt = 1
    elif dist[i] == ans_dist:
        ans_cnt += 1
print(ans, ans_dist, ans_cnt)