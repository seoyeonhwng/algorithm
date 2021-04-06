from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for w in graph[node]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
    return count

N, M = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[b].append(a)

result = {}
for node in range(1, N+1):
    count = bfs(node)
    result[node] = count

result = sorted(result.items(), key=lambda x:(-x[1], x[0]))
count = result[0][1]
for r in result:
    if r[1] == count:
        print(r[0], end=' ')
    else:
        break