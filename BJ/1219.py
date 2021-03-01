from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def check(start):
    stack = [start]
    visited = [False] * N
    visited[start] = True

    while stack:
        node = stack.pop()
        if node == E:
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
                if i == N-1 and check(nxt): # dfs로 돌면서 도착지점이 있는지 확인!!
                    return True
    return False



N, S, E, M = map(int, input().split(' '))
tmp = []
for _ in range(M):
    a, b, c = map(int, input().split(' '))
    tmp.append((a, b, c))
earn = list(map(int, input().split(' ')))

edges = []
graph = defaultdict(list)
for a, b, c in tmp:
    edges.append((a, b, -earn[b] + c))
    graph[a].append((b, -earn[b] + c))

dist = [sys.maxsize] * N
dist[S] = -earn[S]

is_cycle = bf()
if dist[E] == sys.maxsize:
    print('gg')
elif is_cycle:
    print('Gee')
else:
    print(-dist[E])