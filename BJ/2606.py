import collections

def dfs(v):
    path.append(v)
    for w in graph[v]:
        if w not in path:
            dfs(w)

N = int(input())
graph = collections.defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

path = []
dfs(1)
print(len(path)-1)