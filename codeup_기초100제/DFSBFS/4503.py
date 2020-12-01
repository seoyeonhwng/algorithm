import collections

def dfs(graph, v, discovered):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            dfs(graph, w, discovered)


N = input()
M = input()
graph = collections.defaultdict(list)

for i in range(int(M)):
    a, b = input().split(' ')
    graph[a].append(b)
    graph[b].append(a)

discovered = []
dfs(graph, '1', discovered)

print(len(discovered)-1)