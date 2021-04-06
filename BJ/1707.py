from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([(start, 1)])
    visited[start] = 1

    while queue:
        node, color = queue.popleft()

        for w in graph[node]:
            if visited[w] == color:
                return False
            if visited[w] == 0:
                queue.append((w, -color))
                visited[w] = -color
    return True

for _ in range(int(input())):
    V, E = map(int, input().split(' '))
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    visited, ans = [0] * (V+1), True
    for node in range(1, V+1):
        if visited[node] == 0:
            if not bfs(node):
                ans = False
                break
    print('YES') if ans else print('NO')