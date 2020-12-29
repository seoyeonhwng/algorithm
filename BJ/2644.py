import collections

def bfs(start, end):
    path = [start]
    queue = [start]
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            v = queue.pop(0)
            if v == end:
                return depth - 1

            for w in graph[v]:
                if w not in path:
                    path.append(w)
                    queue.append(w)
    return -1


N = int(input())
start, end = map(int, input().split(' '))
graph = collections.defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

# 두 노드 사이의 최단 거리 -> BFS의 depth!
print(bfs(start, end))