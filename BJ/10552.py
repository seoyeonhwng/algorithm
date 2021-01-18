import sys
sys.setrecursionlimit(100000)

def dfs(n):
    global is_circle
    if n in path:
        is_circle = True
        return

    path.add(n)
    if n in graph:
        dfs(graph[n])
    
N, M, P = map(int, input().split(' '))

graph = {}
for _ in range(N):
    a, b = map(int, input().split(' '))
    if b not in graph:
        graph[b] = a

is_circle, path = False, set()
dfs(P)
print(-1) if is_circle else print(len(path)-1)