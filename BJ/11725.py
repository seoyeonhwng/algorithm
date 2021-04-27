from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node):
    for w in graph[node]:
        if path[w] == 0:
            path[w] = node
            dfs(w)


N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

path = [0] * (N+1)
dfs(1)
for i in range(2, N+1):
    print(path[i])