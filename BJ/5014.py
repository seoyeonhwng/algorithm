import collections

# S에서 G로 최단 거리로 이동 -> BFS
def bfs(start):
    queue = collections.deque([(start, 0)])
    visited = set([start])

    while queue:
        v, depth = queue.popleft()
        if v == G:
            return depth

        for w in [v + U, v - D]:
            if (1 <= w <= F) and (w not in visited):
                queue.append((w, depth + 1))
                visited.add(w)
                
    return 'use the stairs'


F, S, G, U, D = map(int, input().split(' '))
print(bfs(S))