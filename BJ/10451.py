import sys
sys.setrecursionlimit(100000)

def dfs(v):
    visited.add(v)
    if nodes[v-1] not in visited:
        dfs(nodes[v-1])

T = int(input())
for _ in range(T):
    N = int(input())
    nodes = list(map(int, input().split(' ')))
    visited = set()

    count = 0
    for n in nodes:
        if n not in visited:
            dfs(n)
            count += 1
    print(count)