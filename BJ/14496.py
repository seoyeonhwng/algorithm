from collections import defaultdict, deque

def bfs():
    # a부터 b까지 최단거리
    queue = deque([(a, 0)])
    visited = set([a])

    while queue:
        node, count = queue.popleft()
        if node == b:
            return count
        
        for w in graph[node]:
            if w not in visited:
                queue.append((w, count + 1))
                visited.add(w)
    return -1

a, b = map(int, input().split(' '))
N, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

print(bfs())
