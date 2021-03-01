import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def check(start):
    stack = [start]
    visited = [False] * (N+1)
    visited[start] = True

    while stack:
        node = stack.pop()
        if node == N:
            return True

        for w, _ in graph[node]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
    return False

def bf():
    for i in range(N):
        for j in range(M):
            cur, nxt, cost = edges[j]
            if dist[cur] != sys.maxsize and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                pred[nxt] = cur
                if i == N-1 and check(nxt): # 가는 경로에 사이클이 있는 경우만 해당됨!!
                    return True
    return False

N, M = map(int, input().rstrip().split(' '))
edges = []
graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().rstrip().split(' '))
    edges.append((u, v, -w))
    graph[u].append((v, w))

dist = [sys.maxsize] * (N+1)
dist[1] = 0
pred = [-1] * (N+1)
is_cycle = bf()

if is_cycle or dist[N] == sys.maxsize:
    print(-1)
else:
    node, ans = N, deque([N])
    while pred[node] != -1:
        node = pred[node]
        ans.appendleft(node)
    print(*ans)
